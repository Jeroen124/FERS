from typing import Optional
from fers_core.members.material import Material


class Section:
    _section_counter = 1

    def __init__(
        self,
        name: str,
        material: Material,
        I_y: float,
        I_z: float,
        area: float,
        h: float = None,
        b: float = None,
        t_w: float = None,
        t_f: float = None,
        id: Optional[int] = None,
    ):
        """
        Initializes a Section object representing a structural element.
        Parameters:
        id (int, optional): Unique identifier for the section.
        name (str): Descriptive name of the section.
        material (Material): Material object representing the type of material used (e.g., steel).
        I_y (float): Moment of inertia about the y-axis, indicating resistance to bending.
        I_z (float): Moment of inertia about the z-axis, indicating resistance to torsion.
        area (float): Cross-sectional area of the section, relevant for load calculations.
        h (float, optional): Height of the section, if applicable.
        b (float, optional): Width of the section, if applicable.
        t_w (float, optional): Thickness of the web, if applicable (default is None).
        t_f (float, optional): Thickness of the flange, if applicable (default is None).
        """
        self.id = id or Section._section_counter
        if id is None:
            Section._section_counter += 1
        self.name = name
        self.material = material
        self.h = h
        self.b = b
        self.I_y = I_y
        self.I_z = I_z
        self.area = area
        self.t_w = t_w
        self.t_f = t_f

    @classmethod
    def reset_counter(cls):
        cls._section_counter = 1
