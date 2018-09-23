/*
 * main_win.cc
 *
 * Copyright 2017-2018 Giuseppe Penone <giuspen@gmail.com>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 */

#include <glibmm/i18n.h>
#include <iostream>
#include "ct_app.h"
#include "p7za_iface.h"


TheTreeView::TheTreeView()
{
    set_headers_visible(false);
}

TheTreeView::~TheTreeView()
{
}


TheTextView::TheTextView()
{
    set_smart_home_end(Gsv::SMART_HOME_END_AFTER);
    set_left_margin(7);
    set_right_margin(7);
}

TheTextView::~TheTextView()
{
}


MainWindow::MainWindow() : Gtk::ApplicationWindow()
{
    _scrolledwindowTree.set_policy(Gtk::POLICY_AUTOMATIC, Gtk::POLICY_AUTOMATIC);
    _scrolledwindowText.set_policy(Gtk::POLICY_AUTOMATIC, Gtk::POLICY_AUTOMATIC);
    _scrolledwindowTree.add(_theTreeview);
    _scrolledwindowText.add(_theTextview);
    _vboxText.pack_start(_scrolledwindowText);
    if (CTApplication::P_ct_config->m_tree_right_side)
    {
        _hPaned.add1(_vboxText);
        _hPaned.add2(_scrolledwindowTree);
    }
    else
    {
        _hPaned.add1(_scrolledwindowTree);
        _hPaned.add2(_vboxText);
    }
    _vboxMain.pack_start(_hPaned);
    add(_vboxMain);
    _theTreestore.view_append_columns(&_theTreeview);
    _theTreestore.view_connect(&_theTreeview);
    _theTreeview.signal_cursor_changed().connect(sigc::mem_fun(*this, &MainWindow::_on_theTreeview_signal_cursor_changed));
    set_size_request(963, 630);
    configApply();
    show_all();
}

MainWindow::~MainWindow()
{
}

void MainWindow::configApply()
{
    _hPaned.property_position() = CTApplication::P_ct_config->m_hpaned_pos;
}

bool MainWindow::readNodesFromGioFile(const Glib::RefPtr<Gio::File>& r_file)
{
    std::string filepath{r_file->get_path()};
    const gchar* pFilepath{NULL};
    if ( (Glib::str_has_suffix(filepath, ".ctz")) ||
         (Glib::str_has_suffix(filepath, ".ctx")) )
    {
        gchar* title = g_strdup_printf(_("Enter Password for %s"), Glib::path_get_basename(filepath).c_str());
        while (true)
        {
            CTDialogTextEntry dialogTextEntry(title, true/*forPassword*/, this);
            int response = dialogTextEntry.run();
            if (Gtk::RESPONSE_OK != response)
            {
                break;
            }
            Glib::ustring password = dialogTextEntry.getEntryText();
            if (0 == p7za_extract(filepath.c_str(),
                                   CTApplication::P_ctTmp->getHiddenDirPath(filepath),
                                   password.c_str()) &&
                g_file_test(CTApplication::P_ctTmp->getHiddenFilePath(filepath), G_FILE_TEST_IS_REGULAR))
            {
                pFilepath = CTApplication::P_ctTmp->getHiddenFilePath(filepath);
                break;
            }
        }
        g_free(title);
    }
    else if ( (Glib::str_has_suffix(filepath, ".ctd")) ||
              (Glib::str_has_suffix(filepath, ".ctb")) )
    {
        pFilepath = filepath.c_str();
    }
    return NULL == pFilepath ? false : _theTreestore.readNodesFromFilepath(pFilepath);
}

void MainWindow::_on_theTreeview_signal_cursor_changed()
{
    Gtk::TreeIter treeIter = _theTreeview.get_selection()->get_selected();
    std::cout << _theTreestore.getNodeName(treeIter) << std::endl;
}


CTDialogTextEntry::CTDialogTextEntry(const char *title, const bool forPassword, Gtk::Window* pParent)
{
    set_title(title);
    set_transient_for(*pParent);
    set_modal();

    add_button(Gtk::Stock::OK, Gtk::RESPONSE_OK);
    add_button(Gtk::Stock::CANCEL, Gtk::RESPONSE_CANCEL);

    _entry.set_icon_from_stock(Gtk::Stock::CLEAR, Gtk::ENTRY_ICON_SECONDARY);
    _entry.set_size_request(350, -1);
    if (forPassword)
    {
        _entry.set_visibility(false);
    }
    get_vbox()->pack_start(_entry, true, true, 0);

    _entry.signal_key_press_event().connect(sigc::mem_fun(*this, &CTDialogTextEntry::on_entry_key_press_event), false);
    _entry.signal_icon_press().connect(sigc::mem_fun(*this, &CTDialogTextEntry::on_entry_icon_press));

    get_vbox()->show_all();
}

CTDialogTextEntry::~CTDialogTextEntry()
{
}

bool CTDialogTextEntry::on_entry_key_press_event(GdkEventKey *eventKey)
{
    if(GDK_KEY_Return == eventKey->keyval)
    {
        Gtk::Button *pButton = static_cast<Gtk::Button*>(get_widget_for_response(Gtk::RESPONSE_OK));
        pButton->clicked();
        return true;
    }
    return false;
}

void CTDialogTextEntry::on_entry_icon_press(Gtk::EntryIconPosition iconPosition, const GdkEventButton* event)
{
    _entry.set_text("");
}

Glib::ustring CTDialogTextEntry::getEntryText()
{
    return _entry.get_text();
}
