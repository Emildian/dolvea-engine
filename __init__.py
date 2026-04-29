# do imports here so I can do a single line import
from pathlib import Path
from textwrap import dedent
import math
import random
import time
from copy import copy, deepcopy
from math import floor, ceil, inf

from dovea.window import instance as window
from dovea.camera import instance as camera
from dovea.mouse import instance as mouse
from dovea.scene import instance as scene
from dovea.main import dovea as dovea
from dovea.main import dovea
from panda3d.core import Mat3, Mat4
from dovea.doveamath import *
from dovea.destroy import destroy
from dovea.doveastuff import *
from dovea.array_tools import *
from dovea import input_handler
from dovea.input_handler import held_keys, Keys
from dovea.string_utilities import *
from dovea.mesh_importer import load_model, load_blender_scene
from dovea.texture import Texture
from dovea.texture_importer import load_texture
from dovea import color
from dovea.color import Color, hsv, rgb
from dovea.sequence import Sequence, Func, Wait
from dovea import curve
from dovea.entity import Entity
from dovea.collider import *
from dovea.raycast import raycast
from dovea.boxcast import boxcast
from dovea.audio import Audio
from dovea import music_system
from dovea.duplicate import duplicate
from panda3d.core import Quat
from dovea.vec2 import Vec2
from dovea.vec3 import Vec3
from dovea.vec4 import Vec4
from dovea.shader import Shader
from dovea.lights import *

from dovea.text import Text
from dovea.mesh import Mesh, MeshModes
from dovea.models.procedural.nine_slice import NineSlice

from dovea.prefabs.sprite import Sprite
from dovea.prefabs.button import Button
from dovea.prefabs.panel import Panel
from dovea.prefabs.sprite_sheet_animation import SpriteSheetAnimation
from dovea.prefabs.animation import Animation
from dovea.prefabs.frame_animation_3d import FrameAnimation3d
from dovea.prefabs.animator import Animator
from dovea.prefabs.sky import Sky
from dovea.prefabs.cursor import Cursor

from dovea.models.procedural.quad import Quad
from dovea.models.procedural.plane import Plane
from dovea.models.procedural.circle import Circle
from dovea.models.procedural.pipe import Pipe
from dovea.models.procedural.cone import Cone
from dovea.models.procedural.cube import Cube
from dovea.models.procedural.cylinder import Cylinder
from dovea.models.procedural.capsule import Capsule
from dovea.models.procedural.grid import Grid
from dovea.models.procedural.terrain import Terrain

from dovea.terraincast import terraincast
from dovea.scripts.smooth_follow import SmoothFollow
from dovea.scripts.grid_layout import grid_layout
from dovea.scripts.scrollable import Scrollable
from dovea.scripts.property_generator import generate_properties_for_class
from dovea.scripts.every_decorator import every

from dovea.prefabs.tooltip import Tooltip
from dovea.prefabs.text_field import TextField
from dovea.prefabs.input_field import InputField, ContentTypes
from dovea.prefabs.draggable import Draggable
from dovea.prefabs.slider import Slider, ThinSlider
from dovea.prefabs.button_group import ButtonGroup
from dovea.prefabs.window_panel import WindowPanel, Space
from dovea.prefabs.button_list import ButtonList
from dovea.prefabs.checkbox import Checkbox
# from dovea.prefabs.file_browser import FileBrowser
# from dovea.prefabs import primitives

# from dovea.prefabs.debug_menu import DebugMenu
from dovea.prefabs.editor_camera import EditorCamera
# from dovea.prefabs.hot_reloader import HotReloader

