import bpy

def executeCommands():
	pass
	bpy.ops.view3d.pastebuffer()
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Omah Jimbaran']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Omah Jimbaran']
	bpy.ops.object.editmode_toggle()
	bpy.ops.object.editmode_toggle()
	bpy.ops.object.editmode_toggle()
	bpy.ops.object.editmode_toggle()
