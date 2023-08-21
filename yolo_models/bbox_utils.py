import numpy as np

from .image_utils import PadInfo, ScaleInfo


def restore_original_coordinates_inplace(bbox_xywh: np.ndarray, pad_info: PadInfo):
    bbox_xywh[:, :2] -= (pad_info.pad_left, pad_info.pad_top)
    return bbox_xywh


def yolo_bbox2xywh_inplace(yolo_xywh_bboxes: np.ndarray):
    yolo_xywh_bboxes[:, 0] = yolo_xywh_bboxes[:, 0] - yolo_xywh_bboxes[:, 2] / 2
    yolo_xywh_bboxes[:, 1] = yolo_xywh_bboxes[:, 1] - yolo_xywh_bboxes[:, 3] / 2
    return yolo_xywh_bboxes

def xyhw2xyxy_inplace(xy2wh: np.ndarray):
    xy2wh[:, 2] += xy2wh[:, 0]
    xy2wh[:, 3] += xy2wh[:, 1]

    return xy2wh

def clip_boxes_inplace(boxes: np.ndarray, width: int, height: int):
    """
    It takes a list of bounding boxes and a shape (height, width) and clips the bounding boxes to the
    shape

    Args:
      boxes: the bounding boxes to clip
      width: image width
      height: image height
    """
    boxes[..., [0, 2]] = boxes[..., [0, 2]].clip(0, width)  # x1, x2
    boxes[..., [1, 3]] = boxes[..., [1, 3]].clip(0, height)  # y1, y2


def scale_bbox_inplace(bbox: np.ndarray, scale_info: ScaleInfo):
    bbox *= (scale_info.to_orig_scale_width, scale_info.to_orig_scale_height,
             scale_info.to_orig_scale_width, scale_info.to_orig_scale_height)
    return bbox
