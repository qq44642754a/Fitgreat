// Auto-generated. Do not edit!

// (in-package easy_handeye_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

let SampleList = require('../msg/SampleList.js');

//-----------------------------------------------------------

class TakeSampleRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TakeSampleRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TakeSampleRequest
    let len;
    let data = new TakeSampleRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'easy_handeye_msgs/TakeSampleRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TakeSampleRequest(null);
    return resolved;
    }
};

class TakeSampleResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.samples = null;
    }
    else {
      if (initObj.hasOwnProperty('samples')) {
        this.samples = initObj.samples
      }
      else {
        this.samples = new SampleList();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TakeSampleResponse
    // Serialize message field [samples]
    bufferOffset = SampleList.serialize(obj.samples, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TakeSampleResponse
    let len;
    let data = new TakeSampleResponse(null);
    // Deserialize message field [samples]
    data.samples = SampleList.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += SampleList.getMessageSize(object.samples);
    return length;
  }

  static datatype() {
    // Returns string type for a service object
    return 'easy_handeye_msgs/TakeSampleResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7d95fb9676bbeca74481a1f545ed96b0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    SampleList samples
    
    ================================================================================
    MSG: easy_handeye_msgs/SampleList
    geometry_msgs/Transform[] hand_world_samples
    geometry_msgs/Transform[] camera_marker_samples
    ================================================================================
    MSG: geometry_msgs/Transform
    # This represents the transform between two coordinate frames in free space.
    
    Vector3 translation
    Quaternion rotation
    
    ================================================================================
    MSG: geometry_msgs/Vector3
    # This represents a vector in free space. 
    # It is only meant to represent a direction. Therefore, it does not
    # make sense to apply a translation to it (e.g., when applying a 
    # generic rigid transformation to a Vector3, tf2 will only apply the
    # rotation). If you want your data to be translatable too, use the
    # geometry_msgs/Point message instead.
    
    float64 x
    float64 y
    float64 z
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TakeSampleResponse(null);
    if (msg.samples !== undefined) {
      resolved.samples = SampleList.Resolve(msg.samples)
    }
    else {
      resolved.samples = new SampleList()
    }

    return resolved;
    }
};

module.exports = {
  Request: TakeSampleRequest,
  Response: TakeSampleResponse,
  md5sum() { return '7d95fb9676bbeca74481a1f545ed96b0'; },
  datatype() { return 'easy_handeye_msgs/TakeSample'; }
};
