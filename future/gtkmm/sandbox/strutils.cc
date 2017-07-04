/*
 * strutils.cc
 * 
 * Copyright 2017 giuspen <giuspen@gmail.com>
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

// https://developer.gnome.org/glib/stable/glib-String-Utility-Functions.html
// g++ strutils.cc -o strutils `pkg-config glibmm-2.4 --cflags --libs`

#include <assert.h>
#include <iostream>
#include <glibmm.h>


std::list<Glib::ustring> ustring_split(const gchar *in_str, const gchar *delimiter, gint max_tokens=-1)
{
    std::list<Glib::ustring> ret_list;
    gchar** array_of_strings = g_strsplit(in_str, delimiter, max_tokens);
    for(gchar** ptr = array_of_strings; *ptr; ptr++)
    {
        ret_list.push_back(*ptr);
    }
    g_strfreev(array_of_strings);
    return ret_list;
}


Glib::ustring ustring_join(std::list<Glib::ustring>& in_str_list, const gchar *delimiter)
{
    Glib::ustring ret_str;
    bool first_iteration = true;
    for(Glib::ustring element : in_str_list)
    {
        if(!first_iteration) ret_str += delimiter;
        else first_iteration = false;
        ret_str += element;
    }
    return ret_str;
}


int main(int argc, char *argv[])
{
    std::locale::global(std::locale("")); // Set the global C++ locale to the user-specified locale

    const gchar str_orig[] = ":a:bc::d:";
    const gchar str_delimiter[] = ":";

    std::cout << str_orig << std::endl;
    std::list<Glib::ustring> splitted_list = ustring_split(str_orig, str_delimiter);
    for(Glib::ustring str_elem : splitted_list)
    {
        std::cout << str_elem << std::endl;
    }
    Glib::ustring rejoined = ustring_join(splitted_list, str_delimiter);
    std::cout << rejoined << std::endl;

    assert(rejoined == str_orig);
}
