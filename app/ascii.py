import datetime # pragma: no cover
import urllib2 # pragma: no cover
import requests # pragma: no cover
import json # pragma: no cover
import logging
from app import app, db, cache # pragma: no cover
from app.models import AsciiArt # pragma: no cover
from app.forms import AsciiForm # pragma: no cover
from flask import render_template, request, url_for, redirect, flash # pragma: no cover


def get_ip():
    headers_list = request.headers.getlist("X-Forwarded-For")
    user_ip = headers_list[0] if headers_list else request.remote_addr
    return user_ip

IP_URL = "http://ip-api.com/json/"
def get_coords(ip):
    ip = get_ip()
    try:
        url = IP_URL + ip
    except TypeError:
        url = IP_URL + "73.55.103.114"
    content = None
    try:
        content = urllib2.urlopen(url).read()
    except URLError:
        return
    if content:
        try:
            result = json.loads(content)
            lat = float(result["lat"])
            lon = float(result["lon"])
            return (lat,lon)
        except KeyError:
            lat = "29.00"
            lon = "-100.00"
            return (lat,lon)
    else:
        return None


def gmaps_img(points):
    GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=550x400&zoom=3&sensor=false"
    for lat, lon in points:
        GMAPS_URL += '&markers=%s,%s' % (lat, lon)
    return GMAPS_URL


def top_arts(update = False):
    key = "top"
    all_art = cache.get(key)
    if all_art is None or update:
        logging.error("DB QUERY")
        all_art = AsciiArt.query.order_by(AsciiArt.id.desc()).all()
        all_art = list(all_art)
        cache.set(key, all_art)
    return all_art


@app.route("/", methods=["GET","POST"])
def hello():
    all_art = top_arts()
    form = AsciiForm()
    ip = get_ip()
    error = None
    lat = [a.lat for a in all_art]
    lon = [b.lon for b in all_art]
    gps = zip(lat,lon)
    img_url = None
    img_url = gmaps_img(gps)
   
    if form.validate_on_submit():
        one = AsciiArt(title=form.title.data, art=form.art.data)
        lat = get_coords(ip)[0]
        lon = get_coords(ip)[1]
        if lat and lon:
            one.lat = lat
            one.lon = lon
        db.session.add(one)
        db.session.commit()
        top_arts(True)
        flash("You just posted some <strong>ascii</strong> artwork!", "success")
        return redirect(url_for("hello"))
    return render_template("front.html", 
        all_art=all_art, 
        img_url=img_url,
        form=form, 
        error=error)


@app.route("/<int:art_id>/edit", methods=["GET","POST"])
def edit_art(art_id):
    all_art = AsciiArt.query.order_by(AsciiArt.id.desc()).all()
    all_art = list(all_art)
    lat = [a.lat for a in all_art]
    lon = [b.lon for b in all_art]
    gps = zip(lat,lon)
    img_url = None
    img_url = gmaps_img(gps)
    error = None
    edit_art = AsciiArt.query.filter_by(id=art_id).one()
    form = AsciiForm(obj=edit_art)
    if form.validate_on_submit():
        edit_art.title = form.title.data
        edit_art.art = form.art.data
        db.session.add(edit_art)
        db.session.commit()
        top_arts(True)
        flash("Successful Edit of <strong>%s</strong>" % edit_art.title, "info")
        return redirect(url_for("hello"))
    return render_template("edit.html", 
        error=error, 
        edit_art=edit_art, 
        form=form, 
        all_art=all_art, 
        img_url=img_url)


@app.route("/<int:art_id>/delete", methods=["GET","POST"])
def delete_art(art_id):
    delete_artwork = AsciiArt.query.filter_by(id=art_id).one()
    form = AsciiForm()
    if request.method == "POST":
        db.session.delete(delete_artwork)
        db.session.commit()
        top_arts(True)
        flash("Just deleted <u>%s</u>" % delete_artwork.title, "danger")
        return redirect(url_for("hello"))
    return render_template("delete.html", 
        delete_artwork=delete_artwork)


@app.route("/ajax", methods=["GET","POST"])
def ajax():    
    return render_template("ajax.html")


@app.route("/puppy-api-example", methods=["GET", "POST"])
def pup_api():
    url = "http://adopt-puppy.herokuapp.com/shelters/.json"
    response = requests.get(url)
    shelters = response.json()
    return render_template("pup-api.html", shelters=shelters)
