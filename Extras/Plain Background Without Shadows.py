import bpy


def extra(data):
    image_scene = data['image_scene']
    camera = data['camera']
    bpy.context.window.scene = image_scene
    bpy.ops.mesh.primitive_plane_add(size=2, location=(0, 0, -3))
    background_plane = bpy.context.active_object
    background_plane.name = 'Light Background'
    modifier = background_plane.modifiers.new(name='', type='SUBSURF')
    modifier.render_levels = 1
    modifier.subdivision_type = 'SIMPLE'
    background_plane.parent = camera
    background_material = bpy.data.materials.new('Light Background')
    background_plane.data.materials.append(background_material)
    background_material.use_nodes = True
    node_tree = background_material.node_tree
    nodes = node_tree.nodes
    for node in nodes:
        if node.type == 'BSDF_PRINCIPLED':
            background_shaded = node
    background_shaded.inputs["Roughness"].default_value = 0.4
    background_shaded.inputs["Base Color"].default_value = (1, 1, 1, 1)

