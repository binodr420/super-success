# Load the layer containing the houses and roads
houses_layer = iface.addVectorLayer('/path/to/houses.shp', 'Houses', 'ogr')
roads_layer = iface.addVectorLayer('/path/to/roads.shp', 'Roads', 'ogr')

# Create a dictionary to store the house numbers for each road
house_numbers = {}

# Loop through each road feature in the roads layer
for road_feature in roads_layer.getFeatures():
    # Get the geometry and attributes for the current road
    road_geom = road_feature.geometry()
    road_id = road_feature['id']
    
    # Split the road geometry into segments
    segments = road_geom.asPolyline()
    
    # Loop through each house feature in the houses layer
    for house_feature in houses_layer.getFeatures():
        # Get the geometry and attributes for the current house
        house_geom = house_feature.geometry()
        house_id = house_feature['id']
        
        # Calculate the distance from the house to the centerline of the road
        distance = road_geom.distance(house_geom)
        
        # Determine which side of the road the house is on
        if house_geom.asPoint().x() < road_geom.interpolate(0.5).asPoint().x():
            side = 'left'
        else:
            side = 'right'
        
        # Determine if the house number is odd or even
        if side == 'left':
            if distance % 2 == 0:
                house_number = int(distance / 2) * -1
            else:
                house_number = int((distance - 1) / 2) * -1
        else:
            if distance % 2 == 0:
                house_number = int(distance / 2)
            else:
                house_number = int((distance - 1) / 2)
        
        # Add the house number to the dictionary for the current road
        if road_id not in house_numbers:
            house_numbers[road_id] = {}
        house_numbers[road_id][house_id] = house_number
        
# Add the house numbers as a new field in the houses layer
houses_layer.startEditing()
houses_layer.addAttribute(QgsField('HouseNumber', QVariant.Int))
for house_feature in houses_layer.getFeatures():
    road_id = house_feature['RoadId']
    house_id = house_feature['id']
    house_number = house_numbers[road_id][house_id]
    houses_layer.changeAttributeValue(house_feature.id(), houses_layer.fields().indexFromName('HouseNumber'), house_number)
houses_layer.commitChanges()