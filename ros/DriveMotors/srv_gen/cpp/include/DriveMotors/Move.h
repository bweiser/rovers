/* Auto-generated by genmsg_cpp for file /opt/projects/adler/planetxrobots/ros/DriveMotors/srv/Move.srv */
#ifndef DRIVEMOTORS_SERVICE_MOVE_H
#define DRIVEMOTORS_SERVICE_MOVE_H
#include <string>
#include <vector>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/message.h"
#include "ros/time.h"

#include "ros/service_traits.h"




namespace DriveMotors
{
template <class ContainerAllocator>
struct MoveRequest_ : public ros::Message
{
  typedef MoveRequest_<ContainerAllocator> Type;

  MoveRequest_()
  : leftSpeed(0)
  , rightSpeed(0)
  , secondsDuration(0)
  , acceleration(0)
  {
  }

  MoveRequest_(const ContainerAllocator& _alloc)
  : leftSpeed(0)
  , rightSpeed(0)
  , secondsDuration(0)
  , acceleration(0)
  {
  }

  typedef int16_t _leftSpeed_type;
  int16_t leftSpeed;

  typedef int16_t _rightSpeed_type;
  int16_t rightSpeed;

  typedef uint16_t _secondsDuration_type;
  uint16_t secondsDuration;

  typedef uint16_t _acceleration_type;
  uint16_t acceleration;


private:
  static const char* __s_getDataType_() { return "DriveMotors/MoveRequest"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "451c087bf7cd0b5ee063409877e152e9"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getServerMD5Sum_() { return "69ab499da909d189bb9422ee7dce103d"; }
public:
  ROS_DEPRECATED static const std::string __s_getServerMD5Sum() { return __s_getServerMD5Sum_(); }

  ROS_DEPRECATED const std::string __getServerMD5Sum() const { return __s_getServerMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
int16 leftSpeed\n\
int16 rightSpeed\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
uint16 secondsDuration\n\
\n\
\n\
\n\
\n\
\n\
\n\
uint16 acceleration\n\
\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, leftSpeed);
    ros::serialization::serialize(stream, rightSpeed);
    ros::serialization::serialize(stream, secondsDuration);
    ros::serialization::serialize(stream, acceleration);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, leftSpeed);
    ros::serialization::deserialize(stream, rightSpeed);
    ros::serialization::deserialize(stream, secondsDuration);
    ros::serialization::deserialize(stream, acceleration);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(leftSpeed);
    size += ros::serialization::serializationLength(rightSpeed);
    size += ros::serialization::serializationLength(secondsDuration);
    size += ros::serialization::serializationLength(acceleration);
    return size;
  }

  typedef boost::shared_ptr< ::DriveMotors::MoveRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::DriveMotors::MoveRequest_<ContainerAllocator>  const> ConstPtr;
}; // struct MoveRequest
typedef  ::DriveMotors::MoveRequest_<std::allocator<void> > MoveRequest;

typedef boost::shared_ptr< ::DriveMotors::MoveRequest> MoveRequestPtr;
typedef boost::shared_ptr< ::DriveMotors::MoveRequest const> MoveRequestConstPtr;


template <class ContainerAllocator>
struct MoveResponse_ : public ros::Message
{
  typedef MoveResponse_<ContainerAllocator> Type;

  MoveResponse_()
  : succeeded(false)
  {
  }

  MoveResponse_(const ContainerAllocator& _alloc)
  : succeeded(false)
  {
  }

  typedef uint8_t _succeeded_type;
  uint8_t succeeded;


private:
  static const char* __s_getDataType_() { return "DriveMotors/MoveResponse"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "95e696a0d10686913abb262e0b4cbbcf"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getServerMD5Sum_() { return "69ab499da909d189bb9422ee7dce103d"; }
public:
  ROS_DEPRECATED static const std::string __s_getServerMD5Sum() { return __s_getServerMD5Sum_(); }

  ROS_DEPRECATED const std::string __getServerMD5Sum() const { return __s_getServerMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "\n\
\n\
\n\
\n\
bool succeeded\n\
\n\
\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, succeeded);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, succeeded);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(succeeded);
    return size;
  }

  typedef boost::shared_ptr< ::DriveMotors::MoveResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::DriveMotors::MoveResponse_<ContainerAllocator>  const> ConstPtr;
}; // struct MoveResponse
typedef  ::DriveMotors::MoveResponse_<std::allocator<void> > MoveResponse;

typedef boost::shared_ptr< ::DriveMotors::MoveResponse> MoveResponsePtr;
typedef boost::shared_ptr< ::DriveMotors::MoveResponse const> MoveResponseConstPtr;

struct Move
{

typedef MoveRequest Request;
typedef MoveResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct Move
} // namespace DriveMotors

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator>
struct MD5Sum< ::DriveMotors::MoveRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "451c087bf7cd0b5ee063409877e152e9";
  }

  static const char* value(const  ::DriveMotors::MoveRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x451c087bf7cd0b5eULL;
  static const uint64_t static_value2 = 0xe063409877e152e9ULL;
};

template<class ContainerAllocator>
struct DataType< ::DriveMotors::MoveRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "DriveMotors/MoveRequest";
  }

  static const char* value(const  ::DriveMotors::MoveRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::DriveMotors::MoveRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
int16 leftSpeed\n\
int16 rightSpeed\n\
\n\
\n\
\n\
\n\
\n\
\n\
\n\
uint16 secondsDuration\n\
\n\
\n\
\n\
\n\
\n\
\n\
uint16 acceleration\n\
\n\
";
  }

  static const char* value(const  ::DriveMotors::MoveRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::DriveMotors::MoveRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator>
struct MD5Sum< ::DriveMotors::MoveResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "95e696a0d10686913abb262e0b4cbbcf";
  }

  static const char* value(const  ::DriveMotors::MoveResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x95e696a0d1068691ULL;
  static const uint64_t static_value2 = 0x3abb262e0b4cbbcfULL;
};

template<class ContainerAllocator>
struct DataType< ::DriveMotors::MoveResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "DriveMotors/MoveResponse";
  }

  static const char* value(const  ::DriveMotors::MoveResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::DriveMotors::MoveResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
\n\
\n\
\n\
bool succeeded\n\
\n\
\n\
";
  }

  static const char* value(const  ::DriveMotors::MoveResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::DriveMotors::MoveResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::DriveMotors::MoveRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.leftSpeed);
    stream.next(m.rightSpeed);
    stream.next(m.secondsDuration);
    stream.next(m.acceleration);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct MoveRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::DriveMotors::MoveResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.succeeded);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct MoveResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<DriveMotors::Move> {
  static const char* value() 
  {
    return "69ab499da909d189bb9422ee7dce103d";
  }

  static const char* value(const DriveMotors::Move&) { return value(); } 
};

template<>
struct DataType<DriveMotors::Move> {
  static const char* value() 
  {
    return "DriveMotors/Move";
  }

  static const char* value(const DriveMotors::Move&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<DriveMotors::MoveRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "69ab499da909d189bb9422ee7dce103d";
  }

  static const char* value(const DriveMotors::MoveRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<DriveMotors::MoveRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "DriveMotors/Move";
  }

  static const char* value(const DriveMotors::MoveRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<DriveMotors::MoveResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "69ab499da909d189bb9422ee7dce103d";
  }

  static const char* value(const DriveMotors::MoveResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<DriveMotors::MoveResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "DriveMotors/Move";
  }

  static const char* value(const DriveMotors::MoveResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // DRIVEMOTORS_SERVICE_MOVE_H

