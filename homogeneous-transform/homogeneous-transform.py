import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here

    points = np.asarray(points)
    if points.ndim == 1:
        points = np.reshape(points, (1, -1))

    transformed_points = [] 
    for point in points:
        homogeneous_point = np.append(point, 1)
        transformed_point = T @ homogeneous_point
        transformed_points.append(transformed_point[:3])

    transformed_points = np.array(transformed_points)

    if transformed_points.shape[0] == 1:
        return transformed_points[0]
    return np.array(transformed_points)