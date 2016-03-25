# -*- coding: UTF-8 -*-
#
#       menus.py
#
#       Copyright 2009-2016 Giuseppe Penone <giuspen@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import cons


def load_menudict(dad):
    """Loads the Menus Dictionary"""
    dad.menudict = {
# sk = stock; sd = short description; kb = keyboard shortcut, dn = description, cb = callback
"NewInstance": {"sk": "new-instance", "sd": _("New _Instance"), "kb": None, "dn": _("Start a New Instance of CherryTree"), "cb": dad.file_new},
"OpenFile": {"sk": "gtk-open", "sd": _("_Open File"), "kb": "<control>O", "dn": _("Open a CherryTree Document"), "cb": dad.file_open},
"Save": {"sk": "gtk-save", "sd": _("_Save"), "kb": "<control>S", "dn": _("Save File"), "cb": dad.file_save},
"SaveAs": {"sk": "gtk-save-as", "sd": _("Save _As"), "kb": "<control><shift>S", "dn": _("Save File As"), "cb": dad.file_save_as},
"OpenCfgFolder": {"sk": "gtk-directory", "sd": _("Open Preferences _Directory"), "kb": None, "dn": _("Open the Directory with Preferences Files"), "cb": dad.folder_cfg_open},
"PrintPageSetup": {"sk": "gtk-print", "sd": _("Pa_ge Setup"), "kb": "<control><shift>P", "dn": _("Set up the Page for Printing"), "cb": dad.export_print_page_setup},
"DoPrint": {"sk": "gtk-print", "sd": _("_Print"), "kb": "<control>P", "dn": _("Print"), "cb": dad.export_print},
"QuitApp": {"sk": "quit-app", "sd": _("_Quit"), "kb": "<control>Q", "dn": _("Quit the Application"), "cb": dad.quit_application},
"ExitApp": {"sk": "quit-app", "sd": _("_Exit CherryTree"), "kb": "<control><shift>Q", "dn": _("Exit from CherryTree"), "cb": dad.quit_application_totally},
"PreferencesDlg": {"sk": "gtk-preferences", "sd": _("_Preferences"), "kb": "<control><alt>P", "dn": _("Preferences"), "cb": dad.dialog_preferences},
"Undo": {"sk": "gtk-undo", "sd": _("_Undo"), "kb": "<control>Z", "dn": _("Undo Last Operation"), "cb": dad.requested_step_back},
"Redo": {"sk": "gtk-redo", "sd": _("_Redo"), "kb": "<control>Y", "dn": _("Redo Previously Discarded Operation"), "cb": dad.requested_step_ahead},
"HandleImage": {"sk": "image_insert", "sd": _("Insert I_mage"), "kb": "<control><alt>I", "dn": _("Insert an Image"), "cb": dad.image_handle},
"HandleTable": {"sk": "table_insert", "sd": _("Insert _Table"), "kb": "<control><alt>T", "dn": _("Insert a Table"), "cb": dad.table_handle},
"HandleCodeBox": {"sk": "codebox_insert", "sd": _("Insert _CodeBox"), "kb": "<control><alt>C", "dn": _("Insert a CodeBox"), "cb": dad.codebox_handle},
"EmbFileInsert": {"sk": "file_icon", "sd": _("Insert _File"), "kb": "<control><alt>E", "dn": _("Insert File"), "cb": dad.embfile_insert},
"HandleLink": {"sk": "link_handle", "sd": _("Insert/Edit _Link"), "kb": "<control>L", "dn": _("Insert a Link/Edit the Underlying Link"), "cb": dad.apply_tag_link},
"HandleAnchor": {"sk": "anchor_insert", "sd": _("Insert _Anchor"), "kb": "<control><alt>A", "dn": _("Insert an Anchor"), "cb": dad.anchor_handle},
"InsertTOC": {"sk": "index", "sd": _("Insert T_OC"), "kb": None, "dn": _("Insert Table of Contents"), "cb": dad.toc_insert},
"Timestamp": {"sk": "timestamp", "sd": _("Insert Ti_mestamp"), "kb": "<control><alt>M", "dn": _("Insert Timestamp"), "cb": dad.timestamp_insert},
"HorizontalRule": {"sk": "horizontal_rule", "sd": _("Insert _Horizontal Rule"), "kb": "<control>R", "dn": _("Insert Horizontal Rule"), "cb": dad.horizontal_rule_insert},
"DownCase": {"sk": "case_lower", "sd": _("_Lower Case of Selection/Word"), "kb": "<control>W", "dn": _("Lower the Case of the Selection/the Underlying Word"), "cb": dad.text_selection_lower_case},
"UpCase": {"sk": "case_upper", "sd": _("_Upper Case of Selection/Word"), "kb": "<control><shift>W", "dn": _("Upper the Case of the Selection/the Underlying Word"), "cb": dad.text_selection_upper_case},
"ToggleCase": {"sk": "case_toggle", "sd": _("_Toggle Case of Selection/Word"), "kb": "<control>G", "dn": _("Toggle the Case of the Selection/the Underlying Word"), "cb": dad.text_selection_toggle_case},
"EnaDisSpellCheck": {"sk": "gtk-spell-check", "sd": _("Enable/Disable _Spell Check"), "kb": "<control><alt>S", "dn": _("Toggle Enable/Disable Spell Check"), "cb": dad.toggle_ena_dis_spellcheck},
"CutPlainText": {"sk": "edit-cut", "sd": _("Cu_t as Plain Text"), "kb": "<control><shift>X", "dn": _("Cut as Plain Text, Discard the Rich Text Formatting"), "cb": dad.cut_as_plain_text},
"CopyPlainText": {"sk": "edit-copy", "sd": _("_Copy as Plain Text"), "kb": "<control><shift>C", "dn": _("Copy as Plain Text, Discard the Rich Text Formatting"), "cb": dad.copy_as_plain_text},
"PastePlainText": {"sk": "edit-paste", "sd": _("_Paste as Plain Text"), "kb": "<control><shift>V", "dn": _("Paste as Plain Text, Discard the Rich Text Formatting"), "cb": dad.paste_as_plain_text},
"CutRow": {"sk": "edit-cut", "sd": _("Cu_t Row"), "kb": "<shift><alt>X", "dn": _("Cut the Current Row/Selected Rows"), "cb": dad.text_row_cut},
"CopyRow": {"sk": "edit-copy", "sd": _("_Copy Row"), "kb": "<shift><alt>C", "dn": _("Copy the Current Row/Selected Rows"), "cb": dad.text_row_copy},
"DeleteRow": {"sk": "edit-delete", "sd": _("De_lete Row"), "kb": "<control>K", "dn": _("Delete the Current Row/Selected Rows"), "cb": dad.text_row_delete},
"DuplicateRow": {"sk": "gtk-add", "sd": _("_Duplicate Row"), "kb": "<control>D", "dn": _("Duplicate the Current Row/Selection"), "cb": dad.text_row_selection_duplicate},
"MoveRowUp": {"sk": "gtk-go-up", "sd": _("Move _Up Row"), "kb": "<alt>Up", "dn": _("Move Up the Current Row/Selected Rows"), "cb": dad.text_row_up},
"MoveRowDown": {"sk": "gtk-go-down", "sd": _("Move _Down Row"), "kb": "<alt>Down", "dn": _("Move Down the Current Row/Selected Rows"), "cb": dad.text_row_down},
"FormatLatest": {"sk": "format_text_latest", "sd": _("Format _Latest"), "kb": "F7", "dn": _("Memory of Latest Text Format Type"), "cb": dad.apply_tag_latest},
"RemoveFormatting": {"sk": "format_text_clear", "sd": _("_Remove Formatting"), "kb": "<control><shift>R", "dn": _("Remove the Formatting from the Selected Text"), "cb": dad.remove_text_formatting},
"ColorForeground": {"sk": "color_foreground", "sd": _("Text _Color Foreground"), "kb": "<shift><alt>F", "dn": _("Change the Color of the Selected Text Foreground"), "cb": dad.apply_tag_foreground},
"ColorBackground": {"sk": "color_background", "sd": _("Text C_olor Background"), "kb": "<shift><alt>B", "dn": _("Change the Color of the Selected Text Background"), "cb": dad.apply_tag_background},
"Bold": {"sk": "format-text-bold", "sd": _("Toggle _Bold Property"), "kb": "<control>B", "dn": _("Toggle Bold Property of the Selected Text"), "cb": dad.apply_tag_bold},
"Italic": {"sk": "format-text-italic", "sd": _("Toggle _Italic Property"), "kb": "<control>I", "dn": _("Toggle Italic Property of the Selected Text"), "cb": dad.apply_tag_italic},
"Underline": {"sk": "format-text-underline", "sd": _("Toggle _Underline Property"), "kb": "<control>U", "dn": _("Toggle Underline Property of the Selected Text"), "cb": dad.apply_tag_underline},
"Strikethrough": {"sk": "format-text-strikethrough", "sd": _("Toggle Stri_kethrough Property"), "kb": "<control>E", "dn": _("Toggle Strikethrough Property of the Selected Text"), "cb": dad.apply_tag_strikethrough},
"H1": {"sk": "format-text-large", "sd": _("Toggle h_1 Property"), "kb": "<control>1", "dn": _("Toggle h1 Property of the Selected Text"), "cb": dad.apply_tag_h1},
"H2": {"sk": "format-text-large2", "sd": _("Toggle h_2 Property"), "kb": "<control>2", "dn": _("Toggle h2 Property of the Selected Text"), "cb": dad.apply_tag_h2},
"H3": {"sk": "format-text-large3", "sd": _("Toggle h_3 Property"), "kb": "<control>3", "dn": _("Toggle h3 Property of the Selected Text"), "cb": dad.apply_tag_h3},
"Small": {"sk": "format-text-small", "sd": _("Toggle _Small Property"), "kb": "<control>0", "dn": _("Toggle Small Property of the Selected Text"), "cb": dad.apply_tag_small},
"Superscript": {"sk": "format-text-superscript", "sd": _("Toggle Su_perscript Property"), "kb": None, "dn": _("Toggle Superscript Property of the Selected Text"), "cb": dad.apply_tag_superscript},
"Subscript": {"sk": "format-text-subscript", "sd": _("Toggle Su_bscript Property"), "kb": None, "dn": _("Toggle Subscript Property of the Selected Text"), "cb": dad.apply_tag_subscript},
"Monospace": {"sk": "format-text-monospace", "sd": _("Toggle _Monospace Property"), "kb": "<control>M", "dn": _("Toggle Monospace Property of the Selected Text"), "cb": dad.apply_tag_monospace},
"BulletedList": {"sk": "list_bulleted", "sd": _("Set/Unset _Bulleted List"), "kb": "<control><alt>1", "dn": _("Set/Unset the Current Paragraph/Selection as a Bulleted List"), "cb": dad.list_bulleted_handler},
"NumberedList": {"sk": "list_numbered", "sd": _("Set/Unset _Numbered List"), "kb": "<control><alt>2", "dn": _("Set/Unset the Current Paragraph/Selection as a Numbered List"), "cb": dad.list_numbered_handler},
"ToDoList": {"sk": "list_todo", "sd": _("Set/Unset _To-Do List"), "kb": "<control><alt>3", "dn": _("Set/Unset the Current Paragraph/Selection as a To-Do List"), "cb": dad.list_todo_handler},
"JustifyLeft": {"sk": "gtk-justify-left", "sd": _("Justify _Left"), "kb": None, "dn": _("Justify Left the Current Paragraph"), "cb": dad.apply_tag_justify_left},
"JustifyCenter": {"sk": "gtk-justify-center", "sd": _("Justify _Center"), "kb": None, "dn": _("Justify Center the Current Paragraph"), "cb": dad.apply_tag_justify_center},
"JustifyRight": {"sk": "gtk-justify-right", "sd": _("Justify _Right"), "kb": None, "dn": _("Justify Right the Current Paragraph"), "cb": dad.apply_tag_justify_right},
"JustifyFill": {"sk": "gtk-justify-fill", "sd": _("Justify _Fill"), "kb": None, "dn": _("Justify Fill the Current Paragraph"), "cb": dad.apply_tag_justify_fill},
"TreeAddNode": {"sk": "tree-node-add", "sd": _("Add _Node"), "kb": "<control>N", "dn": _("Add a Node having the same Father of the Selected Node"), "cb": dad.node_add},
"TreeAddSubNode": {"sk": "tree-subnode-add", "sd": _("Add _SubNode"), "kb": "<control><shift>N", "dn": _("Add a Child Node to the Selected Node"), "cb": dad.node_child_add},
"TreeDuplicateNode": {"sk": "tree-node-dupl", "sd": _("_Duplicate Node"), "kb": "<control><shift>D", "dn": _("Duplicate the Selected Node"), "cb": dad.node_duplicate},
"NodeEdit": {"sk": "cherry_edit", "sd": _("Change Node _Properties"), "kb": "F2", "dn": _("Edit the Properties of the Selected Node"), "cb": dad.node_edit},
"NodeToggleRO": {"sk": "cherry_edit", "sd": _("Toggle _Read Only"), "kb": "<Ctrl><Alt>R", "dn": _("Toggle the Read Only Property of the Selected Node"), "cb": dad.node_toggle_read_only},
"NodeDate": {"sk": "calendar", "sd": _("Insert Today's Node"), "kb": "F8", "dn": _("Insert a Node with Hierarchy Year/Month/Day"), "cb": dad.node_date},
"TreeInfo": {"sk": "gtk-info", "sd": _("Tree _Info"), "kb": None, "dn": _("Tree Summary Information"), "cb": dad.tree_info},
"NodeUp": {"sk": "gtk-go-up", "sd": _("Node _Up"), "kb": "<shift>Up", "dn": _("Move the Selected Node Up"), "cb": dad.node_up},
"NodeDown": {"sk": "gtk-go-down", "sd": _("Node _Down"), "kb": "<shift>Down", "dn": _("Move the Selected Node Down"), "cb": dad.node_down},
"NodeLeft": {"sk": "gtk-go-back", "sd": _("Node _Left"), "kb": "<shift>Left", "dn": _("Move the Selected Node Left"), "cb": dad.node_left},
"NodeNewFather": {"sk": "gtk-jump-to", "sd": _("Node Change _Father"), "kb": "<shift>Right", "dn": _("Change the Selected Node's Father"), "cb": dad.node_change_father},
"TreeSortAsc": {"sk": "gtk-sort-ascending", "sd": _("Sort Tree _Ascending"), "kb": None, "dn": _("Sort the Tree Ascending"), "cb": dad.tree_sort_ascending},
"TreeSortDesc": {"sk": "gtk-sort-descending", "sd": _("Sort Tree _Descending"), "kb": None, "dn": _("Sort the Tree Descending"), "cb": dad.tree_sort_descending},
"SiblSortAsc": {"sk": "gtk-sort-ascending", "sd": _("Sort Siblings A_scending"), "kb": None, "dn": _("Sort all the Siblings of the Selected Node Ascending"), "cb": dad.node_siblings_sort_ascending},
"SiblSortDesc": {"sk": "gtk-sort-descending", "sd": _("Sort Siblings D_escending"), "kb": None, "dn": _("Sort all the Siblings of the Selected Node Descending"), "cb": dad.node_siblings_sort_descending},
"InheritSyntax": {"sk": "gtk-execute", "sd": _("_Inherit Syntax"), "kb": None, "dn": _("Change the Selected Node's Children Syntax Highlighting to the Father's Syntax Highlighting"), "cb": dad.node_inherit_syntax},
"NodeDel": {"sk": "edit-delete", "sd": _("De_lete Node"), "kb": "Delete", "dn": _("Delete the Selected Node"), "cb": dad.node_delete},
"GoBack": {"sk": "gtk-go-back", "sd": _("Go _Back"), "kb": "<alt>Left", "dn": _("Go to the Previous Visited Node"), "cb": dad.go_back},
"GoForward": {"sk": "gtk-go-forward", "sd": _("Go _Forward"), "kb": "<alt>Right", "dn": _("Go to the Next Visited Node"), "cb": dad.go_forward},
"FindInNode": {"sk": "find", "sd": _("_Find in Node Content"), "kb": "<control>F", "dn": _("Find into the Selected Node Content"), "cb": dad.find_in_selected_node},
"FindInNodes": {"sk": "find", "sd": _("Find in _All Nodes Contents"), "kb": "<control><shift>F", "dn": _("Find into All the Tree Nodes Contents"), "cb": dad.find_in_all_nodes},
"FindInSelNSub": {"sk": "find", "sd": _("Find in _Selected Node and Subnodes Contents"), "kb": "<control><alt>F", "dn": _("Find into the Selected Node and Subnodes Contents"), "cb": dad.find_in_sel_node_and_subnodes},
"FindNode": {"sk": "find", "sd": _("Find in _Nodes Names and Tags"), "kb": "<control>T", "dn": _("Find in Nodes Names and Tags"), "cb": dad.find_a_node},
"FindAgain": {"sk": "find_again", "sd": _("Find _Again"), "kb": "F3", "dn": _("Iterate the Last Find Operation"), "cb": dad.find_again},
"FindBack": {"sk": "find_back", "sd": _("Find _Back"), "kb": "F4", "dn": _("Iterate the Last Find Operation in Opposite Direction"), "cb": dad.find_back},
"ReplaceInNode": {"sk": "find_replace", "sd": _("_Replace in Node Content"), "kb": "<control>H", "dn": _("Replace into the Selected Node Content"), "cb": dad.replace_in_selected_node},
"ReplaceInNodes": {"sk": "find_replace", "sd": _("Replace in _All Nodes Contents"), "kb": "<control><shift>H", "dn": _("Replace into All the Tree Nodes Contents"), "cb": dad.replace_in_all_nodes},
"ReplaceInSelNSub": {"sk": "find_replace", "sd": _("Replace in _Selected Node and Subnodes Contents"), "kb": "<control><alt>H", "dn": _("Replace into the Selected Node and Subnodes Contents"), "cb": dad.replace_in_sel_node_and_subnodes},
"ReplaceInNodesNames": {"sk": "find_replace", "sd": _("Replace in Nodes _Names"), "kb": "<control><shift>T", "dn": _("Replace in Nodes Names"), "cb": dad.replace_in_nodes_names},
"ReplaceAgain": {"sk": "find_replace", "sd": _("Replace _Again"), "kb": "F6", "dn": _("Iterate the Last Replace Operation"), "cb": dad.replace_again},
"ShowHideTree": {"sk": "cherries", "sd": _("Show/Hide _Tree"), "kb": "F9", "dn": _("Toggle Show/Hide Tree"), "cb": dad.toggle_show_hide_tree},
"ShowHideToolbar": {"sk": "toolbar", "sd": _("Show/Hide Tool_bar"), "kb": None, "dn": _("Toggle Show/Hide Toolbar"), "cb": dad.toggle_show_hide_toolbar},
"ShowHideNodeNameHeader": {"sk": "node_name_header", "sd": _("Show/Hide Node Name _Header"), "kb": None, "dn": _("Toggle Show/Hide Node Name Header"), "cb": dad.toggle_show_hide_node_name_header},
"ShowAllMatchesDialog": {"sk": "find", "sd": _("Show _All Matches Dialog"), "kb": "<control><shift>A", "dn": _("Show Search All Matches Dialog"), "cb": dad.find_allmatchesdialog_restore},
"ToggleTreeText": {"sk": "gtk-jump-to", "sd": _("Toggle _Focus Tree/Text"), "kb": "<control>Tab", "dn": _("Toggle Focus Between Tree and Text"), "cb": dad.toggle_tree_text},
"ToggleNodeExpColl": {"sk": "gtk-zoom-in", "sd": _("Toggle Node _Expanded/Collapsed"), "kb": "<control><shift>J", "dn": _("Toggle Expanded/Collapsed Status of the Selected Node"), "cb": dad.toggle_tree_node_expanded_collapsed},
"NodesExpAll": {"sk": "gtk-zoom-in", "sd": _("E_xpand All Nodes"), "kb": "<control><shift>E", "dn": _("Expand All the Tree Nodes"), "cb": dad.nodes_expand_all},
"NodesCollAll": {"sk": "gtk-zoom-out", "sd": _("_Collapse All Nodes"), "kb": "<control><shift>L", "dn": _("Collapse All the Tree Nodes"), "cb": dad.nodes_collapse_all},
"IncreaseToolbarIconsSize": {"sk": "gtk-add", "sd": _("_Increase Toolbar Icons Size"), "kb": None, "dn": _("Increase the Size of the Toolbar Icons"), "cb": dad.toolbar_icons_size_increase},
"DecreaseToolbarIconsSize": {"sk": "gtk-remove", "sd": _("_Decrease Toolbar Icons Size"), "kb": None, "dn": _("Decrease the Size of the Toolbar Icons"), "cb": dad.toolbar_icons_size_decrease},
"Fullscreen": {"sk": "gtk-fullscreen", "sd": _("_Full Screen On/Off"), "kb": "F11", "dn": _("Toggle Full Screen On/Off"), "cb": dad.fullscreen_toggle},
"BookmarksHandle": {"sk": "gtk-edit", "sd": _("_Handle Bookmarks"), "kb": None, "dn": _("Handle the Bookmarks List"), "cb": dad.bookmarks_handle},
"FromCherryTree": {"sk": "from_cherrytree", "sd": _("From _CherryTree File"), "kb": None, "dn": _("Add Nodes of a CherryTree File to the Current Tree"), "cb": dad.nodes_add_from_cherrytree_file},
"FromTxtFile": {"sk": "from_txt", "sd": _("From _Plain Text File"), "kb": None, "dn": _("Add Node from a Plain Text File to the Current Tree"), "cb": dad.nodes_add_from_plain_text_file},
"FromTxtFolder": {"sk": "from_txt", "sd": _("From _Folder of Plain Text Files"), "kb": None, "dn": _("Add Nodes from a Folder of Plain Text Files to the Current Tree"), "cb": dad.nodes_add_from_plain_text_folder},
"FromHtmlFile": {"sk": "from_html", "sd": _("From _HTML File"), "kb": None, "dn": _("Add Node from an HTML File to the Current Tree"), "cb": dad.nodes_add_from_html_file},
"FromHtmlFolder": {"sk": "from_html", "sd": _("From _Folder of HTML Files"), "kb": None, "dn": _("Add Nodes from a Folder of HTML Files to the Current Tree"), "cb": dad.nodes_add_from_html_folder},
"FromBasket": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From _Basket Folder"), "kb": None, "dn": _("Add Nodes of a Basket Folder to the Current Tree"), "cb": dad.nodes_add_from_basket_folder},
"FromEPIMHTML": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From _EssentialPIM HTML File"), "kb": None, "dn": _("Add Node from an EssentialPIM HTML File to the Current Tree"), "cb": dad.nodes_add_from_epim_html_file},
"FromGnote": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From _Gnote Folder"), "kb": None, "dn": _("Add Nodes of a Gnote Folder to the Current Tree"), "cb": dad.nodes_add_from_gnote_folder},
"FromKeepNote": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From _KeepNote Folder"), "kb": None, "dn": _("Add Nodes of a KeepNote Folder to the Current Tree"), "cb": dad.nodes_add_from_keepnote_folder},
"FromKeyNote": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From K_eyNote File"), "kb": None, "dn": _("Add Nodes of a KeyNote File to the Current Tree"), "cb": dad.nodes_add_from_keynote_file},
"FromKnowit": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From K_nowit File"), "kb": None, "dn": _("Add Nodes of a Knowit File to the Current Tree"), "cb": dad.nodes_add_from_knowit_file},
"FromLeo": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From _Leo File"), "kb": None, "dn": _("Add Nodes of a Leo File to the Current Tree"), "cb": dad.nodes_add_from_leo_file},
"FromMempad": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From _Mempad File"), "kb": None, "dn": _("Add Nodes of a Mempad File to the Current Tree"), "cb": dad.nodes_add_from_mempad_file},
"FromNoteCase": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From _NoteCase File"), "kb": None, "dn": _("Add Nodes of a NoteCase File to the Current Tree"), "cb": dad.nodes_add_from_notecase_file},
"FromTomboy": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From T_omboy Folder"), "kb": None, "dn": _("Add Nodes of a Tomboy Folder to the Current Tree"), "cb": dad.nodes_add_from_tomboy_folder},
"FromTreepad": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From T_reepad Lite File"), "kb": None, "dn": _("Add Nodes of a Treepad Lite File to the Current Tree"), "cb": dad.nodes_add_from_treepad_file},
"FromTuxCards": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From _TuxCards File"), "kb": None, "dn": _("Add Nodes of a TuxCards File to the Current Tree"), "cb": dad.nodes_add_from_tuxcards_file},
"FromZim": {"sk": cons.STR_STOCK_CT_IMP, "sd": _("From _Zim Folder"), "kb": None, "dn": _("Add Nodes of a Zim Folder to the Current Tree"), "cb": dad.nodes_add_from_zim_folder},
"Export2PDF": {"sk": "to_pdf", "sd": _("Export To _PDF"), "kb": None, "dn": _("Export To PDF"), "cb": dad.export_to_pdf},
"Export2HTML": {"sk": "to_html", "sd": _("Export To _HTML"), "kb": None, "dn": _("Export To HTML"), "cb": dad.export_to_html},
"Export2TxtMultiple": {"sk": "to_txt", "sd": _("Export to Multiple Plain _Text Files"), "kb": None, "dn": _("Export to Multiple Plain Text Files"), "cb": dad.export_to_txt_multiple},
"Export2TxtSingle": {"sk": "to_txt", "sd": _("Export to _Single Plain Text File"), "kb": None, "dn": _("Export to Single Plain Text File"), "cb": dad.export_to_txt_single},
"Export2CTD": {"sk": "to_cherrytree", "sd": _("_Export To CherryTree Document"), "kb": None, "dn": _("Export To CherryTree Document"), "cb": dad.export_to_ctd},
"CheckNewer": {"sk": "gtk-network", "sd": _("_Check Newer Version"), "kb": None, "dn": _("Check for a Newer Version"), "cb": dad.check_for_newer_version},
"Help": {"sk": "help-contents", "sd": _("Online _Manual"), "kb": "F1", "dn": _("Application's Online Manual"), "cb": dad.on_help_menu_item_activated},
"About": {"sk": "gtk-about", "sd": _("_About"), "kb": None, "dn": _("About CherryTree"), "cb": dad.dialog_about},
"CutAnchor": {"sk": "edit-cut", "sd": _("C_ut Anchor"), "kb": None, "dn": _("Cut the Selected Anchor"), "cb": dad.anchor_cut},
"CopyAnchor": {"sk": "edit-copy", "sd": _("_Copy Anchor"), "kb": None, "dn": _("Copy the Selected Anchor"), "cb": dad.anchor_copy},
"DeleteAnchor": {"sk": "edit-delete", "sd": _("_Delete Anchor"), "kb": None, "dn": _("Delete the Selected Anchor"), "cb": dad.anchor_delete},
"EditAnchor": {"sk": "anchor_edit", "sd": _("Edit _Anchor"), "kb": None, "dn": _("Edit the Underlying Anchor"), "cb": dad.anchor_edit},
"CutEmbFile": {"sk": "edit-cut", "sd": _("C_ut Embedded File"), "kb": None, "dn": _("Cut the Selected Embedded File"), "cb": dad.embfile_cut},
"CopyEmbFile": {"sk": "edit-copy", "sd": _("_Copy Embedded File"), "kb": None, "dn": _("Copy the Selected Embedded File"), "cb": dad.embfile_copy},
"DeleteEmbFile": {"sk": "edit-delete", "sd": _("_Delete Embedded File"), "kb": None, "dn": _("Delete the Selected Embedded File"), "cb": dad.embfile_delete},
"EmbFileSave": {"sk": "gtk-save-as", "sd": _("Save _As"), "kb": None, "dn": _("Save File As"), "cb": dad.embfile_save},
"EmbFileOpen": {"sk": "gtk-open", "sd": _("_Open File"), "kb": None, "dn": _("Open Embedded File"), "cb": dad.embfile_open},
"SaveImage": {"sk": "image_save", "sd": _("_Save Image as PNG"), "kb": None, "dn": _("Save the Selected Image as a PNG file"), "cb": dad.image_save},
"EditImage": {"sk": "image_edit", "sd": _("_Edit Image"), "kb": None, "dn": _("Edit the Selected Image"), "cb": dad.image_edit},
"CutImage": {"sk": "edit-cut", "sd": _("C_ut Image"), "kb": None, "dn": _("Cut the Selected Image"), "cb": dad.image_cut},
"CopyImage": {"sk": "edit-copy", "sd": _("_Copy Image"), "kb": None, "dn": _("Copy the Selected Image"), "cb": dad.image_copy},
"DeleteImage": {"sk": "edit-delete", "sd": _("_Delete Image"), "kb": None, "dn": _("Delete the Selected Image"), "cb": dad.image_delete},
"EditImageLink": {"sk": "link_handle", "sd": _("Edit _Link"), "kb": None, "dn": _("Edit the Link Associated to the Image"), "cb": dad.image_link_edit},
"DismissImageLink": {"sk": "gtk-clear", "sd": _("D_ismiss Link"), "kb": None, "dn": _("Dismiss the Link Associated to the Image"), "cb": dad.image_link_dismiss},
"ShowHideMainWin": {"sk": cons.APP_NAME, "sd": _("Show/Hide _CherryTree"), "kb": None, "dn": _("Toggle Show/Hide CherryTree"), "cb": dad.toggle_show_hide_main_window},
}

def get_entries(dad):
    """Returns the Menu Entries Given the Class Instance"""
    if not hasattr(dad, "menudict"): load_menudict(dad)
    entries = [
    # name, stock id, label
    ("FileMenu", None, _("_File")),
    ("EditMenu", None, _("_Edit")),
    ("FormattingMenu", None, _("For_matting")),
    ("TreeMenu", None, _("_Tree")),
    ("TreeMoveMenu", "gtk-jump-to", _("Node _Move")),
    ("TreeImportMenu", cons.STR_STOCK_CT_IMP, _("Nodes _Import")),
    ("TreeExportMenu", "export_from_cherrytree", _("Nodes E_xport")),
    ("ChangeCaseMenu", "case_toggle", _("C_hange Case")),
    ("SearchMenu", None, _("_Search")),
    ("ViewMenu", None, _("_View")),
    ("BookmarksMenu", None, _("_Bookmarks")),
    ("ImportMenu", None, _("_Import")),
    ("ExportMenu", None, _("E_xport")),
    ("HelpMenu", None, _("_Help"))]
    for name in dad.menudict.keys():
        # name, stock id, label, accelerator, tooltip, callback
        subdict = dad.menudict[name]
        entries.append((name, subdict["sk"], subdict["sd"], subdict["kb"], subdict["dn"], subdict["cb"]))
    return entries

def get_popup_menu_table(dad):
    """Returns the Menu Entries Given the Class Instance"""
    # stock id, label, accelerator, tooltip, callback |
    # "separator", None, None, None, None |
    # "submenu-start", label, stock id, None, None |
    # "submenu-end", None, None, None, None
    return [
("edit-cut", _("C_ut Table"), None, _("Cut the Selected Table"), dad.tables_handler.table_cut),
("edit-copy", _("_Copy Table"), None, _("Copy the Selected Table"), dad.tables_handler.table_copy),
("edit-delete", _("_Delete Table"), None, _("Delete the Selected Table"), dad.tables_handler.table_delete),
(cons.TAG_SEPARATOR, None, None, None, None),
("gtk-add", _("_Add Row"), "<control>comma", _("Add a Table Row"), dad.tables_handler.table_row_add),
("edit-cut", _("Cu_t Row"), None, _("Cut a Table Row"), dad.tables_handler.table_row_cut),
("edit-copy", _("_Copy Row"), None, _("Copy a Table Row"), dad.tables_handler.table_row_copy),
("edit-paste", _("_Paste Row"), None, _("Paste a Table Row"), dad.tables_handler.table_row_paste),
("edit-delete", _("De_lete Row"), "<control><alt>comma", _("Delete the Selected Table Row"), dad.tables_handler.table_row_delete),
(cons.TAG_SEPARATOR, None, None, None, None),
("gtk-go-up", _("Move Row _Up"), "<control><alt>period", _("Move the Selected Row Up"), dad.tables_handler.table_row_up),
("gtk-go-down", _("Move Row _Down"), "<control>period", _("Move the Selected Row Down"), dad.tables_handler.table_row_down),
("gtk-sort-descending", _("Sort Rows De_scending"), None, _("Sort all the Rows Descending"), dad.tables_handler.table_rows_sort_descending),
("gtk-sort-ascending", _("Sort Rows As_cending"), None, _("Sort all the Rows Ascending"), dad.tables_handler.table_rows_sort_ascending),
(cons.TAG_SEPARATOR, None, None, None, None),
("table_edit", _("_Edit Table Properties"), None, _("Edit the Table Properties"), dad.tables_handler.table_edit_properties),
("table_save", _("_Table Export"), None, _("Export Table as CSV File"), dad.tables_handler.table_export),
]

def get_popup_menu_tree(dad):
    """Returns the Menu Entries Given the Class Instance"""
    # stock id, label, accelerator, tooltip, callback |
    # "separator", None, None, None, None |
    # "submenu-start", label, stock id, None, None |
    # "submenu-end", None, None, None, None
    return [
("tree-node-add", _("Add _Node"), "<control>N", _("Add a Node having the same Father of the Selected Node"), dad.node_add),
("tree-subnode-add", _("Add _SubNode"), "<control><shift>N", _("Add a Child Node to the Selected Node"), dad.node_child_add),
("tree-node-dupl", _("_Duplicate Node"), "<control><shift>D", _("Duplicate the Selected Node"), dad.node_duplicate),
(cons.TAG_SEPARATOR, None, None, None, None),
("cherry_edit", _("Change Node _Properties"), "F2", _("Edit the Properties of the Selected Node"), dad.node_edit),
("cherry_edit", _("Toggle _Read Only"), "<Ctrl><Alt>R", _("Toggle the Read Only Property of the Selected Node"), dad.node_toggle_read_only),
("pin-add", _("Add to _Bookmarks"), "<control><shift>B", _("Add the Current Node to the Bookmarks List"), dad.bookmark_curr_node),
("pin-remove", _("_Remove from Bookmarks"), "<control><alt>B", _("Remove the Current Node from the Bookmarks List"), dad.bookmark_curr_node_remove),
("calendar", _("Insert Today's Node"), "F8", _("Insert a Node with Hierarchy Year/Month/Day"), dad.node_date),
("gtk-info", _("Tree _Info"), None, _("Tree Summary Information"), dad.tree_info),
(cons.TAG_SEPARATOR, None, None, None, None),
("submenu-start", _("Node _Move"), "gtk-jump-to", None, None),
("gtk-go-up", _("Node _Up"), "<shift>Up", _("Move the Selected Node Up"), dad.node_up),
("gtk-go-down", _("Node _Down"), "<shift>Down", _("Move the Selected Node Down"), dad.node_down),
("gtk-go-back", _("Node _Left"), "<shift>Left", _("Move the Selected Node Left"), dad.node_left),
("gtk-jump-to", _("Node Change _Father"), "<shift>Right", _("Change the Selected Node's Father"), dad.node_change_father),
("submenu-end", None, None, None, None),
(cons.TAG_SEPARATOR, None, None, None, None),
("submenu-start", _("Nodes _Sort"), "gtk-sort-ascending", None, None),
("gtk-sort-ascending", _("Sort Tree _Ascending"), None, _("Sort the Tree Ascending"), dad.tree_sort_ascending),
("gtk-sort-descending", _("Sort Tree _Descending"), None, _("Sort the Tree Descending"), dad.tree_sort_descending),
("gtk-sort-ascending", _("Sort Siblings A_scending"), None, _("Sort all the Siblings of the Selected Node Ascending"), dad.node_siblings_sort_ascending),
("gtk-sort-descending", _("Sort Siblings D_escending"), None, _("Sort all the Siblings of the Selected Node Descending"), dad.node_siblings_sort_descending),
("submenu-end", None, None, None, None),
(cons.TAG_SEPARATOR, None, None, None, None),
("find", _("Find in _Nodes Names and Tags"), "<control>T", _("Find in Nodes Names and Tags"), dad.find_a_node),
("find_replace", _("Replace in Nodes _Names"), "<control><shift>T", _("Replace in Nodes Names"), dad.replace_in_nodes_names),
(cons.TAG_SEPARATOR, None, None, None, None),
("submenu-start", _("Nodes _Import"), cons.STR_STOCK_CT_IMP, None, None),
("from_cherrytree", _("From _CherryTree File"), None, _("Add Nodes of a CherryTree File to the Current Tree"), dad.nodes_add_from_cherrytree_file),
("from_txt", _("From _Plain Text File"), None, _("Add Node from a Plain Text File to the Current Tree"), dad.nodes_add_from_plain_text_file),
("from_txt", _("From _Folder of Plain Text Files"), None, _("Add Nodes from a Folder of Plain Text Files to the Current Tree"), dad.nodes_add_from_plain_text_folder),
("from_html", _("From _HTML File"), None, _("Add Node from an HTML File to the Current Tree"), dad.nodes_add_from_html_file),
("from_html", _("From _Folder of HTML Files"), None, _("Add Nodes from a Folder of HTML Files to the Current Tree"), dad.nodes_add_from_html_folder),
(cons.STR_STOCK_CT_IMP, _("From _Basket Folder"), None, _("Add Nodes of a Basket Folder to the Current Tree"), dad.nodes_add_from_basket_folder),
(cons.STR_STOCK_CT_IMP, _("From _Gnote Folder"), None, _("Add Nodes of a Gnote Folder to the Current Tree"), dad.nodes_add_from_gnote_folder),
(cons.STR_STOCK_CT_IMP, _("From _EssentialPIM HTML File"), None, _("Add Node from an EssentialPIM HTML File to the Current Tree"), dad.nodes_add_from_epim_html_file),
(cons.STR_STOCK_CT_IMP, _("From _KeepNote Folder"), None, _("Add Nodes of a KeepNote Folder to the Current Tree"), dad.nodes_add_from_keepnote_folder),
(cons.STR_STOCK_CT_IMP, _("From K_eyNote File"), None, _("Add Nodes of a KeyNote File to the Current Tree"), dad.nodes_add_from_keynote_file),
(cons.STR_STOCK_CT_IMP, _("From K_nowit File"), None, _("Add Nodes of a Knowit File to the Current Tree"), dad.nodes_add_from_knowit_file),
(cons.STR_STOCK_CT_IMP, _("From _Leo File"), None, _("Add Nodes of a Leo File to the Current Tree"), dad.nodes_add_from_leo_file),
(cons.STR_STOCK_CT_IMP, _("From _Mempad File"), None, _("Add Nodes of a Mempad File to the Current Tree"), dad.nodes_add_from_mempad_file),
(cons.STR_STOCK_CT_IMP, _("From _NoteCase File"), None, _("Add Nodes of a NoteCase File to the Current Tree"), dad.nodes_add_from_notecase_file),
(cons.STR_STOCK_CT_IMP, _("From T_omboy Folder"), None, _("Add Nodes of a Tomboy Folder to the Current Tree"), dad.nodes_add_from_tomboy_folder),
(cons.STR_STOCK_CT_IMP, _("From T_reepad Lite File"), None, _("Add Nodes of a Treepad Lite File to the Current Tree"), dad.nodes_add_from_treepad_file),
(cons.STR_STOCK_CT_IMP, _("From _TuxCards File"), None, _("Add Nodes of a TuxCards File to the Current Tree"), dad.nodes_add_from_tuxcards_file),
(cons.STR_STOCK_CT_IMP, _("From _Zim Folder"), None, _("Add Nodes of a Zim Folder to the Current Tree"), dad.nodes_add_from_zim_folder),
("submenu-end", None, None, None, None),
("submenu-start", _("Nodes E_xport"), "export_from_cherrytree", None, None),
("to_pdf", _("Export To _PDF"), None, _("Export To PDF"), dad.export_to_pdf),
("to_txt", _("Export to Multiple Plain _Text Files"), None, _("Export to Multiple Plain Text Files"), dad.export_to_txt_multiple),
("to_txt", _("Export to _Single Plain Text File"), None, _("Export to Single Plain Text File"), dad.export_to_txt_single),
("to_html", _("Export To _HTML"), None, _("Export To HTML"), dad.export_to_html),
("to_cherrytree", _("_Export To CherryTree Document"), None, _("Export To CherryTree Document"), dad.export_to_ctd),
("submenu-end", None, None, None, None),
(cons.TAG_SEPARATOR, None, None, None, None),
("gtk-execute", _("_Inherit Syntax"), None, _("Change the Selected Node's Children Syntax Highlighting to the Father's Syntax Highlighting"), dad.node_inherit_syntax),
(cons.TAG_SEPARATOR, None, None, None, None),
("edit-delete", _("De_lete Node"), "Delete", _("Delete the Selected Node"), dad.node_delete),
(cons.TAG_SEPARATOR, None, None, None, None),
("gtk-go-back", _("Go _Back"), "<alt>Left", _("Go to the Previous Visited Node"), dad.go_back),
("gtk-go-forward", _("Go _Forward"), "<alt>Right", _("Go to the Next Visited Node"), dad.go_forward),
]

def get_popup_menu_entries_text(dad):
    """Returns the Menu Entries Given the Class Instance"""
    # stock id, label, accelerator, tooltip, callback |
    # "separator", None, None, None, None |
    # "submenu-start", label, stock id, None, None |
    # "submenu-end", None, None, None, None
    return [
(cons.TAG_SEPARATOR, None, None, None, None),
("edit-cut", _("Cu_t as Plain Text"), "<control><shift>X", _("Cut as Plain Text, Discard the Rich Text Formatting"), dad.cut_as_plain_text),
("edit-copy", _("_Copy as Plain Text"), "<control><shift>C", _("Copy as Plain Text, Discard the Rich Text Formatting"), dad.copy_as_plain_text),
("edit-paste", _("_Paste as Plain Text"), "<control><shift>V", _("Paste as Plain Text, Discard the Rich Text Formatting"), dad.paste_as_plain_text),
(cons.TAG_SEPARATOR, None, None, None, None),
("submenu-start", _("For_matting") , "format_text", None, None),
("format_text_latest", _("Format _Latest"), "F7", _("Memory of Latest Text Format Type"), dad.apply_tag_latest),
("format_text_clear", _("_Remove Formatting"), "<control><shift>R", _("Remove the Formatting from the Selected Text"), dad.remove_text_formatting),
(cons.TAG_SEPARATOR, None, None, None, None),
("color_foreground", _("Text _Color Foreground"), None, _("Change the Color of the Selected Text Foreground"), dad.apply_tag_foreground),
("color_background", _("Text C_olor Background"), None, _("Change the Color of the Selected Text Background"), dad.apply_tag_background),
("format-text-bold", _("Toggle _Bold Property"), "<control>B", _("Toggle Bold Property of the Selected Text"), dad.apply_tag_bold),
("format-text-italic", _("Toggle _Italic Property"), "<control>I", _("Toggle Italic Property of the Selected Text"), dad.apply_tag_italic),
("format-text-underline", _("Toggle _Underline Property"), "<control>U", _("Toggle Underline Property of the Selected Text"), dad.apply_tag_underline),
("format-text-strikethrough", _("Toggle Stri_kethrough Property"), "<control>E", _("Toggle Strikethrough Property of the Selected Text"), dad.apply_tag_strikethrough),
("format-text-large", _("Toggle h_1 Property"), "<control>1", _("Toggle h1 Property of the Selected Text"), dad.apply_tag_h1),
("format-text-large2", _("Toggle h_2 Property"), "<control>2", _("Toggle h2 Property of the Selected Text"), dad.apply_tag_h2),
("format-text-large3", _("Toggle h_3 Property"), "<control>3", _("Toggle h3 Property of the Selected Text"), dad.apply_tag_h3),
("format-text-small", _("Toggle _Small Property"), "<control>0", _("Toggle Small Property of the Selected Text"), dad.apply_tag_small),
("format-text-superscript", _("Toggle Su_perscript Property"), None, _("Toggle Superscript Property of the Selected Text"), dad.apply_tag_superscript),
("format-text-subscript", _("Toggle Su_bscript Property"), None, _("Toggle Subscript Property of the Selected Text"), dad.apply_tag_subscript),
("format-text-monospace", _("Toggle _Monospace Property"), "<control>M", _("Toggle Monospace Property of the Selected Text"), dad.apply_tag_monospace),
("submenu-end", None, None, None, None),
("submenu-start", _("_Justify") , "gtk-justify-center", None, None),
("gtk-justify-left", _("Justify _Left"), None, _("Justify Left the Current Paragraph"), dad.apply_tag_justify_left),
("gtk-justify-center", _("Justify _Center"), None, _("Justify Center the Current Paragraph"), dad.apply_tag_justify_center),
("gtk-justify-right", _("Justify _Right"), None, _("Justify Right the Current Paragraph"), dad.apply_tag_justify_right),
("gtk-justify-fill", _("Justify _Fill"), None, _("Justify Fill the Current Paragraph"), dad.apply_tag_justify_fill),
("submenu-end", None, None, None, None),
("submenu-start", _("_List") , "list_bulleted", None, None),
("list_bulleted", _("Set/Unset _Bulleted List"), None, _("Set/Unset the Current Paragraph/Selection as a Bulleted List"), dad.list_bulleted_handler),
("list_numbered", _("Set/Unset _Numbered List"), None, _("Set/Unset the Current Paragraph/Selection as a Numbered List"), dad.list_numbered_handler),
("list_todo", _("Set/Unset _To-Do List"), None, _("Set/Unset the Current Paragraph/Selection as a To-Do List"), dad.list_todo_handler),
("submenu-end", None, None, None, None),
(cons.TAG_SEPARATOR, None, None, None, None),
("submenu-start", _("_Insert") , "insert", None, None),
("image_insert", _("Insert I_mage"), "<control><alt>I", _("Insert an Image"), dad.image_handle),
("table_insert", _("Insert _Table"), "<control><alt>T", _("Insert a Table"), dad.table_handle),
("codebox_insert", _("Insert _CodeBox"), "<control><alt>C", _("Insert a CodeBox"), dad.codebox_handle),
("file_icon", _("Insert _File"), "<control><alt>E", _("Insert File"), dad.embfile_insert),
("link_handle", _("Insert/Edit _Link"), "<control>L", _("Insert a Link/Edit the Underlying Link"), dad.apply_tag_link),
("anchor_insert", _("Insert _Anchor"), "<control><alt>A", _("Insert an Anchor"), dad.anchor_handle),
("index", _("Insert T_OC"), None, _("Insert Table of Contents"), dad.toc_insert),
("timestamp", _("Insert Ti_mestamp"), "<control><alt>M", _("Insert Timestamp"), dad.timestamp_insert),
("horizontal_rule", _("Insert _Horizontal Rule"), "<control>R", _("Insert Horizontal Rule"), dad.horizontal_rule_insert),
("submenu-end", None, None, None, None),
("submenu-start", _("C_hange Case") , "case_toggle", None, None),
("case_lower", _("_Lower Case of Selection/Word"), "<control>W", _("Lower the Case of the Selection/the Underlying Word"), dad.text_selection_lower_case),
("case_upper", _("_Upper Case of Selection/Word"), "<control><shift>W", _("Upper the Case of the Selection/the Underlying Word"), dad.text_selection_upper_case),
("case_toggle", _("_Toggle Case of Selection/Word"), "<control>G", _("Toggle the Case of the Selection/the Underlying Word"), dad.text_selection_toggle_case),
("submenu-end", None, None, None, None),
("submenu-start", _("_Row") , "gtk-edit", None, None),
("edit-cut", _("Cu_t Row"), "<shift><alt>X", _("Cut the Current Row/Selected Rows"), dad.text_row_cut),
("edit-copy", _("C_opy Row"), "<shift><alt>C", _("Copy the Current Row/Selected Rows"), dad.text_row_copy),
("edit-delete", _("De_lete Row"), "<control>K", _("Delete the Current Row/Selected Rows"), dad.text_row_delete),
("gtk-add", _("_Duplicate Row"), "<control>D", _("Duplicate the Current Row/Selection"), dad.text_row_selection_duplicate),
("gtk-go-up", _("Move _Up Row"), "<alt>Up", _("Move Up the Current Row/Selected Rows"), dad.text_row_up),
("gtk-go-down", _("Move _Down Row"), "<alt>Down", _("Move Down the Current Row/Selected Rows"), dad.text_row_down),
("submenu-end", None, None, None, None),
(cons.TAG_SEPARATOR, None, None, None, None),
("submenu-start", _("_Search") , "find", None, None),
("find", _("_Find in Node"), "<control>F", _("Find into the Selected Node"), dad.find_in_selected_node),
("find", _("Find in Node_s"), "<control><shift>F", _("Find into all the Tree Nodes"), dad.find_in_all_nodes),
("find", _("Find in _Nodes Names and Tags"), "<control>T", _("Find in Nodes Names and Tags"), dad.find_a_node),
("find_again", _("Find _Again"), "F3", _("Iterate the Last Find Operation"), dad.find_again),
("find_back", _("Find _Back"), "F4", _("Iterate the Last Find Operation in Opposite Direction"), dad.find_back),
("submenu-end", None, None, None, None),
("submenu-start", _("_Replace") , "find_replace", None, None),
("find_replace", _("_Replace in Node"), "<control>H", _("Replace into the Selected Node"), dad.replace_in_selected_node),
("find_replace", _("Replace in Node_s"), "<control><shift>H", _("Replace into all the Tree Nodes"), dad.replace_in_all_nodes),
("find_replace", _("Replace in Nodes _Names"), "<control><shift>T", _("Replace in Nodes Names"), dad.replace_in_nodes_names),
("find_replace", _("Replace _Again"), "F6", _("Iterate the Last Replace Operation"), dad.replace_again),
("submenu-end", None, None, None, None),
]

def get_popup_menu_entries_code(dad):
    """Returns the Menu Entries Given the Class Instance"""
    # stock id, label, accelerator, tooltip, callback |
    # "separator", None, None, None, None |
    # "submenu-start", label, stock id, None, None |
    # "submenu-end", None, None, None, None
    return [
(cons.TAG_SEPARATOR, None, None, None, None),
("submenu-start", _("_Insert") , "insert", None, None),
("timestamp", _("Insert Ti_mestamp"), "<control><alt>M", _("Insert Timestamp"), dad.timestamp_insert),
("horizontal_rule", _("Insert _Horizontal Rule"), "<control>R", _("Insert Horizontal Rule"), dad.horizontal_rule_insert),
("submenu-end", None, None, None, None),
("gtk-clear", _("Stri_p Trailing Spaces"), None, _("Strip Trailing Spaces"), dad.strip_trailing_spaces),
("submenu-start", _("C_hange Case") , "case_toggle", None, None),
("case_lower", _("_Lower Case of Selection/Word"), "<control>W", _("Lower the Case of the Selection/the Underlying Word"), dad.text_selection_lower_case),
("case_upper", _("_Upper Case of Selection/Word"), "<control><shift>W", _("Upper the Case of the Selection/the Underlying Word"), dad.text_selection_upper_case),
("case_toggle", _("_Toggle Case of Selection/Word"), "<control>G", _("Toggle the Case of the Selection/the Underlying Word"), dad.text_selection_toggle_case),
("submenu-end", None, None, None, None),
("submenu-start", _("_Row") , "gtk-edit", None, None),
("edit-cut", _("Cu_t Row"), "<shift><alt>X", _("Cut the Current Row/Selected Rows"), dad.text_row_cut),
("edit-copy", _("C_opy Row"), "<shift><alt>C", _("Copy the Current Row/Selected Rows"), dad.text_row_copy),
("edit-delete", _("De_lete Row"), "<control>K", _("Delete the Current Row/Selected Rows"), dad.text_row_delete),
("gtk-add", _("_Duplicate Row"), "<control>D", _("Duplicate the Current Row/Selection"), dad.text_row_selection_duplicate),
("gtk-go-up", _("Move _Up Row"), "<alt>Up", _("Move Up the Current Row/Selected Rows"), dad.text_row_up),
("gtk-go-down", _("Move _Down Row"), "<alt>Down", _("Move Down the Current Row/Selected Rows"), dad.text_row_down),
("submenu-end", None, None, None, None),
(cons.TAG_SEPARATOR, None, None, None, None),
("submenu-start", _("_Search") , "find", None, None),
("find", _("_Find in Node"), "<control>F", _("Find into the Selected Node"), dad.find_in_selected_node),
("find", _("Find in Node_s"), "<control><shift>F", _("Find into all the Tree Nodes"), dad.find_in_all_nodes),
("find", _("Find in _Nodes Names and Tags"), "<control>T", _("Find in Nodes Names and Tags"), dad.find_a_node),
("find_again", _("Find _Again"), "F3", _("Iterate the Last Find Operation"), dad.find_again),
("find_back", _("Find _Back"), "F4", _("Iterate the Last Find Operation in Opposite Direction"), dad.find_back),
("submenu-end", None, None, None, None),
("submenu-start", _("_Replace") , "find_replace", None, None),
("find_replace", _("_Replace in Node"), "<control>H", _("Replace into the Selected Node"), dad.replace_in_selected_node),
("find_replace", _("Replace in Node_s"), "<control><shift>H", _("Replace into all the Tree Nodes"), dad.replace_in_all_nodes),
("find_replace", _("Replace in Nodes _Names"), "<control><shift>T", _("Replace in Nodes Names"), dad.replace_in_nodes_names),
("find_replace", _("Replace _Again"), "F6", _("Iterate the Last Replace Operation"), dad.replace_again),
("submenu-end", None, None, None, None),
]

def get_popup_menu_entries_link(dad):
    """Returns the Menu Entries Given the Class Instance"""
    # stock id, label, accelerator, tooltip, callback |
    # "separator", None, None, None, None |
    # "submenu-start", label, stock id, None, None |
    # "submenu-end", None, None, None, None
    return [
(cons.TAG_SEPARATOR, None, None, None, None),
("link_handle", _("Edit _Link"), None, _("Edit the Underlying Link"), dad.apply_tag_link),
(cons.TAG_SEPARATOR, None, None, None, None),
("edit-cut", _("C_ut Link"), None, _("Cut the Selected Link"), dad.link_cut),
("edit-copy", _("_Copy Link"), None, _("Copy the Selected Link"), dad.link_copy),
("gtk-clear", _("D_ismiss Link"), None, _("Dismiss the Selected Link"), dad.link_dismiss),
("edit-delete", _("_Delete Link"), None, _("Delete the Selected Link"), dad.link_delete),
]

def get_popup_menu_entries_table_cell(dad):
    """Returns the Menu Entries Given the Class Instance"""
    # stock id, label, accelerator, tooltip, callback |
    # "separator", None, None, None, None |
    # "submenu-start", label, stock id, None, None |
    # "submenu-end", None, None, None, None
    return [
(cons.TAG_SEPARATOR, None, None, None, None),
("insert", _("Insert _NewLine"), "<control>period", _("Insert NewLine Char"), dad.curr_table_cell_insert_newline),
]

def get_popup_menu_entries_codebox(dad):
    """Returns the Menu Entries Given the Class Instance"""
    # stock id, label, accelerator, tooltip, callback |
    # "separator", None, None, None, None |
    # "submenu-start", label, stock id, None, None |
    # "submenu-end", None, None, None, None
    return [
(cons.TAG_SEPARATOR, None, None, None, None),
("codebox_edit", _("Change CodeBox _Properties"), None, _("Edit the Properties of the CodeBox"), dad.codebox_change_properties),
("from_txt", _("CodeBox _Load From Text File"), None, _("Load the CodeBox Content From a Text File"), dad.codebox_load_from_file),
("to_txt", _("CodeBox _Save To Text File"), None, _("Save the CodeBox Content To a Text File"), dad.codebox_save_to_file),
(cons.TAG_SEPARATOR, None, None, None, None),
("edit-cut", _("C_ut CodeBox"), None, _("Cut the Selected CodeBox"), dad.codebox_cut),
("edit-copy", _("_Copy CodeBox"), None, _("Copy the Selected CodeBox"), dad.codebox_copy),
("edit-delete", _("_Delete CodeBox"), None, _("Delete the Selected CodeBox"), dad.codebox_delete),
("edit-delete", _("Delete CodeBox _Keep Content"), None, _("Delete the Selected CodeBox But Keep Its Content"), dad.codebox_delete_keeping_text),
(cons.TAG_SEPARATOR, None, None, None, None),
("gtk-go-forward", _("Increase CodeBox Width"), "<control>period", _("Increase the Width of the CodeBox"), dad.codebox_increase_width),
("gtk-go-back", _("Decrease CodeBox Width"), "<control><alt>period", _("Decrease the Width of the CodeBox"), dad.codebox_decrease_width),
("gtk-go-down", _("Increase CodeBox Height"), "<control>comma", _("Increase the Height of the CodeBox"), dad.codebox_increase_height),
("gtk-go-up", _("Decrease CodeBox Height"), "<control><alt>comma", _("Decrease the Height of the CodeBox"), dad.codebox_decrease_height),
]

UI_INFO = """
<ui>
  <menubar name='MenuBar'>
    <menu action='FileMenu'>
      <menuitem action='NewInstance'/>
      <menuitem action='OpenFile'/>
      <separator/>
      <menuitem action='Save'/>
      <menuitem action='SaveAs'/>
      <separator/>
      <menuitem action='PrintPageSetup'/>
      <menuitem action='DoPrint'/>
      <separator/>
      <menuitem action='QuitApp'/>
      <menuitem action='ExitApp'/>
    </menu>

    <menu action='EditMenu'>
      <menuitem action='PreferencesDlg'/>
      <separator/>
      <menuitem action='Undo'/>
      <menuitem action='Redo'/>
      <separator/>
      <menuitem action='HandleImage'/>
      <menuitem action='HandleTable'/>
      <menuitem action='HandleCodeBox'/>
      <menuitem action='EmbFileInsert'/>
      <menuitem action='HandleLink'/>
      <menuitem action='HandleAnchor'/>
      <menuitem action='InsertTOC'/>
      <menuitem action='Timestamp'/>
      <menuitem action='HorizontalRule'/>
      <separator/>
      <menu action='ChangeCaseMenu'>
        <menuitem action='DownCase'/>
        <menuitem action='UpCase'/>
        <menuitem action='ToggleCase'/>
      </menu>
      <separator/>
      <menuitem action='EnaDisSpellCheck'/>
      <separator/>
      <menuitem action='CutPlainText'/>
      <menuitem action='CopyPlainText'/>
      <menuitem action='PastePlainText'/>
      <separator/>
      <menuitem action='CutRow'/>
      <menuitem action='CopyRow'/>
      <menuitem action='DeleteRow'/>
      <menuitem action='DuplicateRow'/>
      <menuitem action='MoveRowUp'/>
      <menuitem action='MoveRowDown'/>
    </menu>

    <menu action='FormattingMenu'>
      <menuitem action='FormatLatest'/>
      <menuitem action='RemoveFormatting'/>
      <separator/>
      <menuitem action='ColorForeground'/>
      <menuitem action='ColorBackground'/>
      <menuitem action='Bold'/>
      <menuitem action='Italic'/>
      <menuitem action='Underline'/>
      <menuitem action='Strikethrough'/>
      <menuitem action='H1'/>
      <menuitem action='H2'/>
      <menuitem action='H3'/>
      <menuitem action='Small'/>
      <menuitem action='Superscript'/>
      <menuitem action='Subscript'/>
      <menuitem action='Monospace'/>
      <separator/>
      <menuitem action='BulletedList'/>
      <menuitem action='NumberedList'/>
      <menuitem action='ToDoList'/>
      <separator/>
      <menuitem action='JustifyLeft'/>
      <menuitem action='JustifyCenter'/>
      <menuitem action='JustifyRight'/>
      <menuitem action='JustifyFill'/>
    </menu>

    <menu action='TreeMenu'>
    </menu>

    <menu action='SearchMenu'>
      <menuitem action='FindInNode'/>
      <menuitem action='FindInNodes'/>
      <menuitem action='FindInSelNSub'/>
      <menuitem action='FindNode'/>
      <menuitem action='FindAgain'/>
      <menuitem action='FindBack'/>
      <separator/>
      <menuitem action='ReplaceInNode'/>
      <menuitem action='ReplaceInNodes'/>
      <menuitem action='ReplaceInSelNSub'/>
      <menuitem action='ReplaceInNodesNames'/>
      <menuitem action='ReplaceAgain'/>
    </menu>

    <menu action='ViewMenu'>
      <menuitem action='ShowHideTree'/>
      <menuitem action='ShowHideToolbar'/>
      <menuitem action='ShowHideNodeNameHeader'/>
      <menuitem action='ShowAllMatchesDialog'/>
      <separator/>
      <menuitem action='ToggleTreeText'/>
      <menuitem action='ToggleNodeExpColl'/>
      <menuitem action='NodesExpAll'/>
      <menuitem action='NodesCollAll'/>
      <separator/>
      <menuitem action='IncreaseToolbarIconsSize'/>
      <menuitem action='DecreaseToolbarIconsSize'/>
      <separator/>
      <menuitem action='Fullscreen'/>
    </menu>

    <menu action='BookmarksMenu'>
      <menuitem action='BookmarksHandle'/>
    </menu>

    <menu action='ImportMenu'>
      <menuitem action='FromCherryTree'/>
      <menuitem action='FromTxtFile'/>
      <menuitem action='FromTxtFolder'/>
      <menuitem action='FromHtmlFile'/>
      <menuitem action='FromHtmlFolder'/>
      <menuitem action='FromBasket'/>
      <menuitem action='FromEPIMHTML'/>
      <menuitem action='FromGnote'/>
      <menuitem action='FromKeepNote'/>
      <menuitem action='FromKeyNote'/>
      <menuitem action='FromKnowit'/>
      <menuitem action='FromLeo'/>
      <menuitem action='FromMempad'/>
      <menuitem action='FromNoteCase'/>
      <menuitem action='FromTomboy'/>
      <menuitem action='FromTreepad'/>
      <menuitem action='FromTuxCards'/>
      <menuitem action='FromZim'/>
    </menu>

    <menu action='ExportMenu'>
      <menuitem action='Export2PDF'/>
      <menuitem action='Export2HTML'/>
      <menuitem action='Export2TxtMultiple'/>
      <menuitem action='Export2TxtSingle'/>
      <menuitem action='Export2CTD'/>
    </menu>

    <menu action='HelpMenu'>
      <menuitem action='CheckNewer'/>
      <separator/>
      <menuitem action='Help'/>
      <separator/>
      <menuitem action='OpenCfgFolder'/>
      <separator/>
      <menuitem action='About'/>
    </menu>
  </menubar>

  <popup name='SysTrayMenu'>
    <menuitem action='ShowHideMainWin'/>
    <separator/>
    <menuitem action='ExitApp'/>
  </popup>

  <popup name='ImageMenu'>
    <menuitem action='CutImage'/>
    <menuitem action='CopyImage'/>
    <menuitem action='DeleteImage'/>
    <separator/>
    <menuitem action='EditImage'/>
    <menuitem action='SaveImage'/>
    <separator/>
    <menuitem action='EditImageLink'/>
    <menuitem action='DismissImageLink'/>
  </popup>

  <popup name='AnchorMenu'>
    <menuitem action='CutAnchor'/>
    <menuitem action='CopyAnchor'/>
    <menuitem action='DeleteAnchor'/>
    <separator/>
    <menuitem action='EditAnchor'/>
  </popup>

  <popup name='EmbFileMenu'>
    <menuitem action='CutEmbFile'/>
    <menuitem action='CopyEmbFile'/>
    <menuitem action='DeleteEmbFile'/>
    <separator/>
    <menuitem action='EmbFileOpen'/>
    <menuitem action='EmbFileSave'/>
  </popup>
</ui>
"""
