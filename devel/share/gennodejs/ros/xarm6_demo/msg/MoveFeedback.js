// Auto-generated. Do not edit!

// (in-package xarm6_demo.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class MoveFeedback {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.current_pulse = null;
    }
    else {
      if (initObj.hasOwnProperty('current_pulse')) {
        this.current_pulse = initObj.current_pulse
      }
      else {
        this.current_pulse = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MoveFeedback
    // Serialize message field [current_pulse]
    bufferOffset = _serializer.float32(obj.current_pulse, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MoveFeedback
    let len;
    let data = new MoveFeedback(null);
    // Deserialize message field [current_pulse]
    data.current_pulse = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'xarm6_demo/MoveFeedback';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a244e071efec9946f249ffbbf7ee56b0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    
    float32 current_pulse
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MoveFeedback(null);
    if (msg.current_pulse !== undefined) {
      resolved.current_pulse = msg.current_pulse;
    }
    else {
      resolved.current_pulse = 0.0
    }

    return resolved;
    }
};

module.exports = MoveFeedback;