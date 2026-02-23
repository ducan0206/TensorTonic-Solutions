def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here
    anchors = []

    stride = image_size / feature_size

    for i in range(feature_size):
        for j in range(feature_size):
            x_center = (j + 0.5) * stride
            y_center = (i + 0.5) * stride

            for scale in scales:
                for aspect_ratio in aspect_ratios:
                    w = scale * (aspect_ratio ** 0.5)
                    h = scale / (aspect_ratio ** 0.5)

                    anchor = [x_center - w / 2, y_center - h / 2, x_center + w / 2, y_center + h / 2]
                    anchors.append(anchor)

    return anchors