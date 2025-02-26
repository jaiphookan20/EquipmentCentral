from flask import Blueprint, jsonify, request
from app import db
from app.models import Equipment, EquipmentCategory, Operator, User
import math

# Create a Blueprint for API routes
api = Blueprint('api', __name__)

@api.route('/equipment', methods=['GET'])
def get_equipment():
    """Get all equipment"""
    equipment_list = Equipment.query.all()
    result = []
    for equipment in equipment_list:
        result.append({
            'id': equipment.id,
            'name': equipment.name,
            'description': equipment.description,
            'daily_rate': equipment.daily_rate,
            'weekly_rate': equipment.weekly_rate,
            'monthly_rate': equipment.monthly_rate,
            'availability_status': equipment.availability_status
        })
    return jsonify(result)

@api.route('/equipment/nearby', methods=['GET'])
def get_nearby_equipment():
    """Get equipment near a location"""
    # Get parameters
    lat = float(request.args.get('lat', 0))
    lng = float(request.args.get('lng', 0))
    radius = float(request.args.get('radius', 10000))  # Default 10km
    
    # Get all operators
    operators = Operator.query.all()
    nearby_operators = []
    
    # Calculate distance using Haversine formula
    for operator in operators:
        distance = calculate_distance(lat, lng, operator.latitude, operator.longitude)
        if distance <= radius:
            nearby_operators.append(operator.id)
    
    # Get equipment from nearby operators
    equipment_list = Equipment.query.filter(Equipment.operator_id.in_(nearby_operators)).all()
    
    result = []
    for equipment in equipment_list:
        result.append({
            'id': equipment.id,
            'name': equipment.name,
            'description': equipment.description,
            'daily_rate': equipment.daily_rate,
            'weekly_rate': equipment.weekly_rate,
            'monthly_rate': equipment.monthly_rate,
            'availability_status': equipment.availability_status,
            'operator': {
                'id': equipment.operator.id,
                'business_name': equipment.operator.business_name,
                'suburb': equipment.operator.suburb,
                'state': equipment.operator.state
            }
        })
    
    return jsonify(result)

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371000  # Radius of earth in meters
    return c * r
