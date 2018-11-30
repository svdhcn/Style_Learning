#----------------------------------------------------------
# File hello.py
#----------------------------------------------------------
import bpy
 
#
#    Menu in tools region
#
class ToolsPanel(bpy.types.Panel):
    bl_label = "Hello from Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        self.layout.operator("hello.hello")
 
#
#    Menu in toolprops region
#
class ToolPropsPanel(bpy.types.Panel):
    bl_label = "Hello from Tool props"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOL_PROPS"
 
    def draw(self, context):
        self.layout.operator("hello.hello", text='Hej').country = "Sweden"
 
#
#    Menu in UI region
#
class UIPanel(bpy.types.Panel):
    bl_label = "Hello from UI panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
 
    def draw(self, context):
        self.layout.operator("hello.hello", text='Servus')
 
#
#    Menu in window region, object context
#
class ObjectPanel(bpy.types.Panel):
    bl_label = "Hello from Object context"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
 
    def draw(self, context):
        self.layout.operator("hello.hello", text='Bonjour').country = "France"
 
#
#    Menu in window region, material context
#
class MaterialPanel(bpy.types.Panel):
    bl_label = "Hello from Material context"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"
 
    def draw(self, context):
        self.layout.operator("hello.hello", text='Ciao').country = "Italy"
 
#
#    The Hello button prints a message in the console
#
class OBJECT_OT_HelloButton(bpy.types.Operator):
    bl_idname = "hello.hello"
    bl_label = "Say Hello"
    country = bpy.props.StringProperty()
 
    def execute(self, context):
        if self.country == '':
            print("Hello world!")
        else:
            print("Hello world from %s!" % self.country)
        return{'FINISHED'}    
 
#
#	Registration
#   All panels and operators must be registered with Blender; otherwise
#   they do not show up. The simplest way to register everything in the
#   file is with a call to bpy.utils.register_module(__name__).
#
 
bpy.utils.register_module(__name__)