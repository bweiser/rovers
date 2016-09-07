/* Auto-generated by genmsg_cpp for file /opt/projects/adler/planetxrobots/ros/RoverState/msg/Range.msg */
#ifndef ROVERSTATE_MESSAGE_RANGE_H
#define ROVERSTATE_MESSAGE_RANGE_H
#include <string>
#include <vector>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/message.h"
#include "ros/time.h"

#include "std_msgs/Header.h"

namespace RoverState
{
template <class ContainerAllocator>
struct Range_ : public ros::Message
{
  typedef Range_<ContainerAllocator> Type;

  Range_()
  : header()
  , frontRangeCm(0)
  , backRangeCm(0)
  {
  }

  Range_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , frontRangeCm(0)
  , backRangeCm(0)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef uint16_t _frontRangeCm_type;
  uint16_t frontRangeCm;

  typedef uint16_t _backRangeCm_type;
  uint16_t backRangeCm;


private:
  static const char* __s_getDataType_() { return "RoverState/Range"; }
public:
  ROS_DEPRECATED static const std::string __s_getDataType() { return __s_getDataType_(); }

  ROS_DEPRECATED const std::string __getDataType() const { return __s_getDataType_(); }

private:
  static const char* __s_getMD5Sum_() { return "b1976b1487c64c9b4693bb336701082a"; }
public:
  ROS_DEPRECATED static const std::string __s_getMD5Sum() { return __s_getMD5Sum_(); }

  ROS_DEPRECATED const std::string __getMD5Sum() const { return __s_getMD5Sum_(); }

private:
  static const char* __s_getMessageDefinition_() { return "#\n\
# front and read range measurements\n\
#\n\
Header header\n\
uint16 frontRangeCm\n\
uint16 backRangeCm\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
"; }
public:
  ROS_DEPRECATED static const std::string __s_getMessageDefinition() { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED const std::string __getMessageDefinition() const { return __s_getMessageDefinition_(); }

  ROS_DEPRECATED virtual uint8_t *serialize(uint8_t *write_ptr, uint32_t seq) const
  {
    ros::serialization::OStream stream(write_ptr, 1000000000);
    ros::serialization::serialize(stream, header);
    ros::serialization::serialize(stream, frontRangeCm);
    ros::serialization::serialize(stream, backRangeCm);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint8_t *deserialize(uint8_t *read_ptr)
  {
    ros::serialization::IStream stream(read_ptr, 1000000000);
    ros::serialization::deserialize(stream, header);
    ros::serialization::deserialize(stream, frontRangeCm);
    ros::serialization::deserialize(stream, backRangeCm);
    return stream.getData();
  }

  ROS_DEPRECATED virtual uint32_t serializationLength() const
  {
    uint32_t size = 0;
    size += ros::serialization::serializationLength(header);
    size += ros::serialization::serializationLength(frontRangeCm);
    size += ros::serialization::serializationLength(backRangeCm);
    return size;
  }

  typedef boost::shared_ptr< ::RoverState::Range_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::RoverState::Range_<ContainerAllocator>  const> ConstPtr;
}; // struct Range
typedef  ::RoverState::Range_<std::allocator<void> > Range;

typedef boost::shared_ptr< ::RoverState::Range> RangePtr;
typedef boost::shared_ptr< ::RoverState::Range const> RangeConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::RoverState::Range_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::RoverState::Range_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace RoverState

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator>
struct MD5Sum< ::RoverState::Range_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b1976b1487c64c9b4693bb336701082a";
  }

  static const char* value(const  ::RoverState::Range_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xb1976b1487c64c9bULL;
  static const uint64_t static_value2 = 0x4693bb336701082aULL;
};

template<class ContainerAllocator>
struct DataType< ::RoverState::Range_<ContainerAllocator> > {
  static const char* value() 
  {
    return "RoverState/Range";
  }

  static const char* value(const  ::RoverState::Range_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::RoverState::Range_<ContainerAllocator> > {
  static const char* value() 
  {
    return "#\n\
# front and read range measurements\n\
#\n\
Header header\n\
uint16 frontRangeCm\n\
uint16 backRangeCm\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
";
  }

  static const char* value(const  ::RoverState::Range_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::RoverState::Range_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::RoverState::Range_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::RoverState::Range_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.frontRangeCm);
    stream.next(m.backRangeCm);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct Range_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::RoverState::Range_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::RoverState::Range_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "frontRangeCm: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.frontRangeCm);
    s << indent << "backRangeCm: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.backRangeCm);
  }
};


} // namespace message_operations
} // namespace ros

#endif // ROVERSTATE_MESSAGE_RANGE_H

