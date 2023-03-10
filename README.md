# Unreal Engine Asset Remover
# ue-unused-asset-remover
This script allows you to delete or move selected assets in the Unreal Engine Editor.

# Requirements

* Unreal Engine 4.26
* Python 3.7
* ```unreal``` and ```os``` modules

# Installation
1. Clone this repository or download the ZIP archive and extract its contents.
2. Copy and paste it into your Unreal Engine projects script file.

# Usage
1. Select one or more assets in the Content Browser.
2. Go to **File > Execute Python Script**
3. Locate your script in your project's files and run it.

# Notes
* * Be careful when using the Asset Deletion Tool, as it permanently deletes assets. Make sure you have backups of your project before using the tool.
* The Asset Deletion Tool only deletes assets that are not referenced by other assets in the project. If an asset is referenced by other assets, it will not be deleted.
* The Asset Deletion Tool does not support deleting assets that are loaded by a running level. If an asset is loaded by a running level, it will not be deleted.
* The Asset Deletion Tool does not work with assets that are locked in the Content Browser.
