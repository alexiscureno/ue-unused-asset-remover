import unreal
import os


# Instantiate the Unreal Editor Utility and Asset Library classes.
editor_util = unreal.EditorUtilityLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()


# Get the currently selected assets in the Editor.
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
removed = 0

# Choose whether to instantly delete assets or move them to a trash folder.
instant_delete = False
trash_folder = os.path.join(os.sep, "Game", "Trash")
to_be_deleted = []

# Check if the asset has no references.
for asset in selected_assets:
    # Get the full path of the asset.
    asset_name = asset.get_fname()
    asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)

    # Get a list of references for this asset.
    asset_references = editor_asset_lib.find_package_referencers_for_asset(asset_path)

    if len(asset_references) == 0:
        to_be_deleted.append(asset)

# Process the assets in the to_be_deleted list.
for asset in to_be_deleted:

    # Get a list of references for this asset.
    asset_name = asset.get_fname()

    # Instantly delete the assets.
    if instant_delete:
        deleted = editor_asset_lib.delete_loaded_asset(asset)

        # If there are no references, add the asset to the to_be_deleted list.
        if not deleted:
            unreal.log('Asset {} could not be deleted'.format(asset_name))
            continue

        removed += 1
    # Move the assets to a trash folder.
    else:
        new_path = os.path.join(trash_folder, str(asset_name))
        moved = editor_asset_lib.rename_loaded_asset(asset, new_path)

        if not moved:
            unreal.log('Asset {} could not be moved to trash'.format(asset_name))
            continue

        removed += 1
output_test = "removed" if instant_delete else "moved to trash folder"
unreal.log("{} of {} to be deleted assets, of {} selected, removed".format(removed, len(to_be_deleted), num_assets))