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
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
	bpy.ops.object.delete(use_global=False)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Omah Jimbaran']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Omah Jimbaran']
	bpy.ops.object.delete(use_global=False)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Camera']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Camera']
	bpy.ops.object.delete(use_global=False)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Omah Jimbaran']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Omah Jimbaran']
	bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
	bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)
	bpy.ops.view3d.snap_selected_to_cursor(use_offset=True)
	bpy.ops.transform.translate(value=(0, 0, 0.905644), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
	bpy.ops.transform.translate(value=(0, 0, 4.82417), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Cube']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
	bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Sphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Sphere']
	bpy.ops.transform.translate(value=(0, 0, 5.0406), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
<<<<<<< Updated upstream
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Sphere.001']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Sphere.001']
	bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(-3.34937, -0, -0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(True, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "alt_navigation":True, "use_automerge_and_split":False})
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Sphere.002']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Sphere.002']
	bpy.ops.object.duplicate_move_linked(OBJECT_OT_duplicate={"linked":True, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(6.57089, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(True, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "alt_navigation":True, "use_automerge_and_split":False})
=======
	bpy.ops.object.editmode_toggle()
	bpy.ops.object.editmode_toggle()
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['root', 'SKM_Quinn_Simple_LOD1', 'SKM_Quinn_Simple_LOD0', 'SKM_Quinn_Simple_LOD2', 'SKM_Quinn_Simple_LodGroup', 'SKM_Quinn_Simple']]
	bpy.context.view_layer.objects.active = bpy.data.objects['root']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Sphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Sphere']
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Omah Jimbaran']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Omah Jimbaran']
	bpy.ops.outliner.item_activate(deselect_all=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['SKM_Quinn_Simple']]
	bpy.context.view_layer.objects.active = bpy.data.objects['SKM_Quinn_Simple']
	bpy.ops.transform.translate(value=(5.71233, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, alt_navigation=True)
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Omah Jimbaran']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Omah Jimbaran']
	bpy.context.object.rotation_euler[2] = -1.15192
	bpy.context.object.rotation_euler[2] = -1.5708
	[obj.select_set(False) for obj in bpy.context.view_layer.objects.selected.values()]
	[bpy.context.view_layer.objects.get(obj).select_set(True) for obj in ['Sphere']]
	bpy.context.view_layer.objects.active = bpy.data.objects['Sphere']
>>>>>>> Stashed changes
	bpy.ops.object.delete(use_global=False)
