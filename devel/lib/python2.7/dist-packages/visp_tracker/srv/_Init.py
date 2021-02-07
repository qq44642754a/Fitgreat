# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from visp_tracker/InitRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import visp_tracker.msg

class InitRequest(genpy.Message):
  _md5sum = "72f45c4391731722797b61d639ff8889"
  _type = "visp_tracker/InitRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Initialize the tracking.
#
# During the initialization the tracked object is chosen and its
# initial pose is required to start the tracking.
#
# The model is retrieved through the parameter server using the
# model_description parameter.

# Object initial pose.
geometry_msgs/Transform initial_cMo

# Common Tracker Parameters
TrackerSettings tracker_param

# Moving Edge parameters
MovingEdgeSettings moving_edge

# Klt Parameters
KltSettings klt_param

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

================================================================================
MSG: visp_tracker/TrackerSettings
# This message contains tracking parameters.
#
# These parameters determine how precise, how fast and how
# reliable will be the tracking.
#
# It should be tuned carefully and can be changed dynamically.
#
# For more details, see the ViSP documentation:
# http://www.irisa.fr/lagadic/visp/publication.html

# Common Tracker Parameters.
float64 angle_appear    # Angle to test faces apparition
float64 angle_disappear # Angle to test faces disparition


================================================================================
MSG: visp_tracker/MovingEdgeSettings
# This message contains tracking parameters.
#
# These parameters determine how precise, how fast and how
# reliable will be the tracking.
#
# It should be tuned carefully and can be changed dynamically.
#
# For more details, see the ViSP documentation:
# http://www.irisa.fr/lagadic/visp/publication.html


# Moving edge parameters.

int64 mask_size    # Mask size (in pixel) used to compute the image gradient
                   # and determine the object contour.
		   # A larger mask size is better for larger images.
		   # 3 pixels is enough for 640x480 images.
                   # Increasing this value makes the tracking slower.
		   #
		   # Caution: this value cannot be changed dynamically
		   # without resetting the tracking.

int64 range        # Maximum seek distance on both sides of the reference pixel.
      		   # It should match the maximum distance in pixel between
		   # the current position of the feature projection and
		   # its next position.
		   # I.e. if the object moves fast and your tracking
		   # frequency is low, this value should be increased.
                   # Increasing this value makes the tracking slower.

float64 threshold  # Value used to determine if a moving edge is valid
		   # or not.

float64 mu1        # Minimum image contrast allowed to detect a contour.
float64 mu2        # Maximum image contrast allowed to detect a contour.

int64 sample_step   # Minimum distance in pixel between two
      		    # discretization points.
      		    # It avoids having too many discretization points when
		    # the tracked object is far away (and its projection
		    # in the image is small).
		    # Increasing this value makes the tracking *faster*.

int64 strip             # How many pixels are ignored around the borders.


# Tracker parameters.

float64 first_threshold # What proportion of points should be valid to
                        # acccept an initial pose.
			# Value should be between 0 et 1.


================================================================================
MSG: visp_tracker/KltSettings
# This message contains tracking parameters.
#
# These parameters determine how precise, how fast and how
# reliable will be the tracking.
#
# It should be tuned carefully and can be changed dynamically.
#
# For more details, see the ViSP documentation:
# http://www.irisa.fr/lagadic/visp/publication.html

# Klt Parameters.

int64 max_features      # Maximum number of features
int64 window_size       # Window size
float64 quality         # Quality of the tracker
float64 min_distance      # Minimum distance betwenn two points
float64 harris          # Harris free parameters
int64 size_block        # Block size
int64 pyramid_lvl       # Pyramid levels
int64 mask_border       # Mask Border

"""
  __slots__ = ['initial_cMo','tracker_param','moving_edge','klt_param']
  _slot_types = ['geometry_msgs/Transform','visp_tracker/TrackerSettings','visp_tracker/MovingEdgeSettings','visp_tracker/KltSettings']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       initial_cMo,tracker_param,moving_edge,klt_param

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(InitRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.initial_cMo is None:
        self.initial_cMo = geometry_msgs.msg.Transform()
      if self.tracker_param is None:
        self.tracker_param = visp_tracker.msg.TrackerSettings()
      if self.moving_edge is None:
        self.moving_edge = visp_tracker.msg.MovingEdgeSettings()
      if self.klt_param is None:
        self.klt_param = visp_tracker.msg.KltSettings()
    else:
      self.initial_cMo = geometry_msgs.msg.Transform()
      self.tracker_param = visp_tracker.msg.TrackerSettings()
      self.moving_edge = visp_tracker.msg.MovingEdgeSettings()
      self.klt_param = visp_tracker.msg.KltSettings()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_9d2q3d2qd2q3d3q().pack(_x.initial_cMo.translation.x, _x.initial_cMo.translation.y, _x.initial_cMo.translation.z, _x.initial_cMo.rotation.x, _x.initial_cMo.rotation.y, _x.initial_cMo.rotation.z, _x.initial_cMo.rotation.w, _x.tracker_param.angle_appear, _x.tracker_param.angle_disappear, _x.moving_edge.mask_size, _x.moving_edge.range, _x.moving_edge.threshold, _x.moving_edge.mu1, _x.moving_edge.mu2, _x.moving_edge.sample_step, _x.moving_edge.strip, _x.moving_edge.first_threshold, _x.klt_param.max_features, _x.klt_param.window_size, _x.klt_param.quality, _x.klt_param.min_distance, _x.klt_param.harris, _x.klt_param.size_block, _x.klt_param.pyramid_lvl, _x.klt_param.mask_border))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.initial_cMo is None:
        self.initial_cMo = geometry_msgs.msg.Transform()
      if self.tracker_param is None:
        self.tracker_param = visp_tracker.msg.TrackerSettings()
      if self.moving_edge is None:
        self.moving_edge = visp_tracker.msg.MovingEdgeSettings()
      if self.klt_param is None:
        self.klt_param = visp_tracker.msg.KltSettings()
      end = 0
      _x = self
      start = end
      end += 200
      (_x.initial_cMo.translation.x, _x.initial_cMo.translation.y, _x.initial_cMo.translation.z, _x.initial_cMo.rotation.x, _x.initial_cMo.rotation.y, _x.initial_cMo.rotation.z, _x.initial_cMo.rotation.w, _x.tracker_param.angle_appear, _x.tracker_param.angle_disappear, _x.moving_edge.mask_size, _x.moving_edge.range, _x.moving_edge.threshold, _x.moving_edge.mu1, _x.moving_edge.mu2, _x.moving_edge.sample_step, _x.moving_edge.strip, _x.moving_edge.first_threshold, _x.klt_param.max_features, _x.klt_param.window_size, _x.klt_param.quality, _x.klt_param.min_distance, _x.klt_param.harris, _x.klt_param.size_block, _x.klt_param.pyramid_lvl, _x.klt_param.mask_border,) = _get_struct_9d2q3d2qd2q3d3q().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_9d2q3d2qd2q3d3q().pack(_x.initial_cMo.translation.x, _x.initial_cMo.translation.y, _x.initial_cMo.translation.z, _x.initial_cMo.rotation.x, _x.initial_cMo.rotation.y, _x.initial_cMo.rotation.z, _x.initial_cMo.rotation.w, _x.tracker_param.angle_appear, _x.tracker_param.angle_disappear, _x.moving_edge.mask_size, _x.moving_edge.range, _x.moving_edge.threshold, _x.moving_edge.mu1, _x.moving_edge.mu2, _x.moving_edge.sample_step, _x.moving_edge.strip, _x.moving_edge.first_threshold, _x.klt_param.max_features, _x.klt_param.window_size, _x.klt_param.quality, _x.klt_param.min_distance, _x.klt_param.harris, _x.klt_param.size_block, _x.klt_param.pyramid_lvl, _x.klt_param.mask_border))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.initial_cMo is None:
        self.initial_cMo = geometry_msgs.msg.Transform()
      if self.tracker_param is None:
        self.tracker_param = visp_tracker.msg.TrackerSettings()
      if self.moving_edge is None:
        self.moving_edge = visp_tracker.msg.MovingEdgeSettings()
      if self.klt_param is None:
        self.klt_param = visp_tracker.msg.KltSettings()
      end = 0
      _x = self
      start = end
      end += 200
      (_x.initial_cMo.translation.x, _x.initial_cMo.translation.y, _x.initial_cMo.translation.z, _x.initial_cMo.rotation.x, _x.initial_cMo.rotation.y, _x.initial_cMo.rotation.z, _x.initial_cMo.rotation.w, _x.tracker_param.angle_appear, _x.tracker_param.angle_disappear, _x.moving_edge.mask_size, _x.moving_edge.range, _x.moving_edge.threshold, _x.moving_edge.mu1, _x.moving_edge.mu2, _x.moving_edge.sample_step, _x.moving_edge.strip, _x.moving_edge.first_threshold, _x.klt_param.max_features, _x.klt_param.window_size, _x.klt_param.quality, _x.klt_param.min_distance, _x.klt_param.harris, _x.klt_param.size_block, _x.klt_param.pyramid_lvl, _x.klt_param.mask_border,) = _get_struct_9d2q3d2qd2q3d3q().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_9d2q3d2qd2q3d3q = None
def _get_struct_9d2q3d2qd2q3d3q():
    global _struct_9d2q3d2qd2q3d3q
    if _struct_9d2q3d2qd2q3d3q is None:
        _struct_9d2q3d2qd2q3d3q = struct.Struct("<9d2q3d2qd2q3d3q")
    return _struct_9d2q3d2qd2q3d3q
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from visp_tracker/InitResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class InitResponse(genpy.Message):
  _md5sum = "8e1a436e960986e0760f2970d0c88bf4"
  _type = "visp_tracker/InitResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Did the initialization succeed?
bool initialization_succeed

"""
  __slots__ = ['initialization_succeed']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       initialization_succeed

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(InitResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.initialization_succeed is None:
        self.initialization_succeed = False
    else:
      self.initialization_succeed = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.initialization_succeed
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.initialization_succeed,) = _get_struct_B().unpack(str[start:end])
      self.initialization_succeed = bool(self.initialization_succeed)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.initialization_succeed
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.initialization_succeed,) = _get_struct_B().unpack(str[start:end])
      self.initialization_succeed = bool(self.initialization_succeed)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class Init(object):
  _type          = 'visp_tracker/Init'
  _md5sum = '99679e33547ba56c949bb75d2a309602'
  _request_class  = InitRequest
  _response_class = InitResponse