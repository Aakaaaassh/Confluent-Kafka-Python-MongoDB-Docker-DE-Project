#!/usr/bin/env python
# coding: utf-8


from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId  # Import ObjectId from bson
import re

app = Flask(__name__)

# MongoDB configuration
mongo_client = MongoClient('mongodb+srv://user:pass@projectzero.e4ptdtp.mongodb.net/')
db = mongo_client['gds_db']
collection = db['logistic_data']

@app.route('/api/bookingid',methods=['GET'])
def bookings():
    try:
        # Get the value of the 'vehicle_no' query parameter
        BookingID = request.args.get('BookingID')

        if not BookingID:
            return jsonify({"error": "Missing 'BookingID' parameter"}), 400
        
        filter={'BookingID': BookingID}
        collation={}
        sort=list({}.items())
        result = mongo_client['gds_db']['logistic_data'].find(filter=filter,sort=sort)
        result_list = [{'_id': str(doc['_id']), "GpsProvider": doc["GpsProvider"],
            "BookingID": doc["BookingID"],
            "Market/Regular ": doc["Market_Regular"],
            "BookingID_Date": doc["BookingID_Date"],
            "vehicle_no": doc["vehicle_no"],
            "Origin_Location": doc["Origin_Location"],
            "Destination_Location": doc["Destination_Location"],
            "Org_lat_lon": doc["Org_lat_lon"],
            "Des_lat_lon": doc["Des_lat_lon"],
            "Data_Ping_time": doc["Data_Ping_time"],
            "Planned_ETA": doc["Planned_ETA"],
            "Current_Location": doc["Current_Location"],
            "DestinationLocation": doc["DestinationLocation"],
            "actual_eta": doc["actual_eta"],
            "Curr_lat": doc["Curr_lat"],
            "Curr_lon": doc["Curr_lon"],
            "ontime": doc["ontime"],
            "delay": doc["delay"],
            "OriginLocation_Code": doc["OriginLocation_Code"],
            "DestinationLocation_Code": doc["DestinationLocation_Code"],
            "trip_start_date": doc["trip_start_date"],
            "trip_end_date": doc["trip_end_date"],
            "TRANSPORTATION_DISTANCE_IN_KM": doc["TRANSPORTATION_DISTANCE_IN_KM"],
            "vehicleType": doc["vehicleType"],
            "Minimum_kms_to_be_covered_in_a_day": doc["Minimum_kms_to_be_covered_in_a_day"],
            "Driver_Name": doc["Driver_Name"],
            "Driver_MobileNo": doc["Driver_MobileNo"],
            "customerID": doc["customerID"],
            "customerNameCode": doc["customerNameCode"],
            "supplierID": doc["supplierID"],
            "supplierNameCode": doc["supplierNameCode"],
            "Material Shipped": doc["Material_Shipped"]} for doc in result]

        if result_list:
            return jsonify({"result": result_list}), 200
        else:
            return jsonify({"result": "No matching documents found"}), 404

    except Exception as e:
        # Check if the exception has a meaningful error message
        error_message = str(e) if e and str(e) else "An unexpected error occurred."

        # Return a JSON response with the error message and a 500 Internal Server Error status code
        return jsonify({"error": error_message} if error_message else {"error": "An unexpected error occurred."}), 500 

    
    #http://127.0.0.1:5000/api/bookingid?BookingID=AEIBK2022926



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)




