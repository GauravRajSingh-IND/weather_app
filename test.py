# Import Module
from tkinter import *
from tkhtmlview import HTMLLabel

# Create Object
root = Tk()

# Set Geometry
root.geometry("400x400")

# Add label
my_label = HTMLLabel(root, html="""
<!DOCTYPE html>
<html>
<head>
    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_0ef0d120b6ed319a83435f2d66ff4b84 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            </style>
        
</head>
<body>
    
    
            <div class="folium-map" id="map_0ef0d120b6ed319a83435f2d66ff4b84" ></div>
        
</body>
<script>
    
    
            var map_0ef0d120b6ed319a83435f2d66ff4b84 = L.map(
                "map_0ef0d120b6ed319a83435f2d66ff4b84",
                {
                    center: [26.9196, 75.7878],
                    crs: L.CRS.EPSG3857,
                    zoom: 5,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_09c62118e535662477e0dc15794e0094 = L.tileLayer(
                "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors", "detectRetina": false, "maxNativeZoom": 19, "maxZoom": 19, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            );
        
    
            tile_layer_09c62118e535662477e0dc15794e0094.addTo(map_0ef0d120b6ed319a83435f2d66ff4b84);
        
    
            var tile_layer_e3a8f9595573fd4dae1a0b4b1c6e5a1c = L.tileLayer(
                "https://tile.openweathermap.org/map/temp_new/5/{x}/{y}.png?appid=04081e17627f601aa461ea47e4ec87e9",
                {"attribution": "OpenWeatherMap", "detectRetina": false, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            );
        
    
            tile_layer_e3a8f9595573fd4dae1a0b4b1c6e5a1c.addTo(map_0ef0d120b6ed319a83435f2d66ff4b84);
        
    
            var layer_control_4e110a1f7f7f650e20148ea87c2a4e19_layers = {
                base_layers : {
                    "openstreetmap" : tile_layer_09c62118e535662477e0dc15794e0094,
                },
                overlays :  {
                    "Temperature Layer" : tile_layer_e3a8f9595573fd4dae1a0b4b1c6e5a1c,
                },
            };
            let layer_control_4e110a1f7f7f650e20148ea87c2a4e19 = L.control.layers(
                layer_control_4e110a1f7f7f650e20148ea87c2a4e19_layers.base_layers,
                layer_control_4e110a1f7f7f650e20148ea87c2a4e19_layers.overlays,
                {"autoZIndex": true, "collapsed": true, "position": "topright"}
            ).addTo(map_0ef0d120b6ed319a83435f2d66ff4b84);

        
</script>
</html>
    """)

# Adjust label
my_label.pack(pady=20, padx=20)

# Execute Tkinter
root.mainloop()