// Generated by gencpp from file xarm_msgs/SetControllerAnalogIO.msg
// DO NOT EDIT!


#ifndef XARM_MSGS_MESSAGE_SETCONTROLLERANALOGIO_H
#define XARM_MSGS_MESSAGE_SETCONTROLLERANALOGIO_H

#include <ros/service_traits.h>


#include <xarm_msgs/SetControllerAnalogIORequest.h>
#include <xarm_msgs/SetControllerAnalogIOResponse.h>


namespace xarm_msgs
{

struct SetControllerAnalogIO
{

typedef SetControllerAnalogIORequest Request;
typedef SetControllerAnalogIOResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetControllerAnalogIO
} // namespace xarm_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::xarm_msgs::SetControllerAnalogIO > {
  static const char* value()
  {
    return "2b78c87698704b2bc72cea876ba90e55";
  }

  static const char* value(const ::xarm_msgs::SetControllerAnalogIO&) { return value(); }
};

template<>
struct DataType< ::xarm_msgs::SetControllerAnalogIO > {
  static const char* value()
  {
    return "xarm_msgs/SetControllerAnalogIO";
  }

  static const char* value(const ::xarm_msgs::SetControllerAnalogIO&) { return value(); }
};


// service_traits::MD5Sum< ::xarm_msgs::SetControllerAnalogIORequest> should match
// service_traits::MD5Sum< ::xarm_msgs::SetControllerAnalogIO >
template<>
struct MD5Sum< ::xarm_msgs::SetControllerAnalogIORequest>
{
  static const char* value()
  {
    return MD5Sum< ::xarm_msgs::SetControllerAnalogIO >::value();
  }
  static const char* value(const ::xarm_msgs::SetControllerAnalogIORequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::xarm_msgs::SetControllerAnalogIORequest> should match
// service_traits::DataType< ::xarm_msgs::SetControllerAnalogIO >
template<>
struct DataType< ::xarm_msgs::SetControllerAnalogIORequest>
{
  static const char* value()
  {
    return DataType< ::xarm_msgs::SetControllerAnalogIO >::value();
  }
  static const char* value(const ::xarm_msgs::SetControllerAnalogIORequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::xarm_msgs::SetControllerAnalogIOResponse> should match
// service_traits::MD5Sum< ::xarm_msgs::SetControllerAnalogIO >
template<>
struct MD5Sum< ::xarm_msgs::SetControllerAnalogIOResponse>
{
  static const char* value()
  {
    return MD5Sum< ::xarm_msgs::SetControllerAnalogIO >::value();
  }
  static const char* value(const ::xarm_msgs::SetControllerAnalogIOResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::xarm_msgs::SetControllerAnalogIOResponse> should match
// service_traits::DataType< ::xarm_msgs::SetControllerAnalogIO >
template<>
struct DataType< ::xarm_msgs::SetControllerAnalogIOResponse>
{
  static const char* value()
  {
    return DataType< ::xarm_msgs::SetControllerAnalogIO >::value();
  }
  static const char* value(const ::xarm_msgs::SetControllerAnalogIOResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // XARM_MSGS_MESSAGE_SETCONTROLLERANALOGIO_H