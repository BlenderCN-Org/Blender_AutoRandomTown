import bpy
import random


def join_object():
    for ob in bpy.context.scene.objects:
        #�I�u�W�F�N�g�̓��b�V�����H
        if ob.type == 'MESH':
            ob.select = True
            bpy.context.scene.objects.active = ob
        else :
            ob.select = False

    bpy.ops.object.join()
    return


def import_fbx(path_i):
    bpy.ops.import_scene.fbx(filepath=path_i, axis_forward='-Z', axis_up='Y', directory="", filter_glob="*.fbx", ui_tab='MAIN', use_manual_orientation=False, global_scale=1.0, bake_space_transform=False, use_custom_normals=True, use_image_search=True, use_alpha_decals=False, decal_offset=0.0, use_anim=True, anim_offset=1.0, use_custom_props=True, use_custom_props_enum_as_string=True, ignore_leaf_bones=False, force_connect_children=False, automatic_bone_orientation=False, primary_bone_axis='Y', secondary_bone_axis='X', use_prepost_rot=True)
    return

def export_fbx(path_e):
    bpy.ops.export_scene.fbx(filepath=path_e, check_existing=True, axis_forward='-Z', axis_up='Y', filter_glob="*.fbx", version='BIN7400', ui_tab='MAIN', use_selection=False, global_scale=1.0, apply_unit_scale=True, bake_space_transform=False, object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LAMP', 'MESH', 'OTHER'}, use_mesh_modifiers=True, mesh_smooth_type='OFF', use_mesh_edges=False, use_tspace=False, use_custom_props=False, add_leaf_bones=True, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, armature_nodetype='NULL', bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, use_anim=True, use_anim_action_all=True, use_default_take=True, use_anim_optimize=True, anim_optimize_precision=6.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True)
    return

def refresh_obj():
    for x in bpy.data.objects:
        bpy.data.objects.remove(x)
    #�V�[�����̃I�u�W�F�N�g��S�ď���

        
def refresh_mat():
    for x in bpy.data.materials:
        bpy.data.materials.remove(x)
    #�V�[�����̃}�e���A����S�ď���(���t���b�V��)

def refresh_tex():
    for x in bpy.data.textures:
        bpy.data.textures.remove(x)

def refresh():
    refresh_obj()
    refresh_mat()
    refresh_tex()
    #�S�����t���b�V��

def rename():
    for x in bpy.data.objects:
        x.name = 'obj'
    #�V�[�����̃I�u�W�F�N�g�̖��O��'obj'�ɓ���

def name_mat():
    count = 0;
    for x in bpy.data.materials:
        if (len(x.texture_slots)!=0):
            x.name = bpy.data.textures[x.texture_slots[0].texture.name].image.filepath[-9:-4]



path = 'D:\\TBA\\main\\test.fbx'


#���s����

refresh()
path_test = 'D:\\TBA\\test_plane\\tes.fbx'
for x in range(20):

    import_fbx(path_test)
    
    path_e = 'D:\\TBA\\result\\'+str(x)+'.fbx'
    #path_e = '/home/taisyo/TBA/result/' + str(x) + '.fbx'
    join_object()
    rename()
    name_mat()
    export_fbx(path_e)
    refresh()




