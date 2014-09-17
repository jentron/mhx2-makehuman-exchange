#
#    MakeProxy - Utility for making proxy meshes.
#    Like MakeClothes but slightly newer
#    Copyright (C) Thomas Larsson 2014
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import bpy

theMessage = "No message"
theErrorLines = []

class ErrorOperator(bpy.types.Operator):
    bl_idname = "mhpxy.error"
    bl_label = "Error using MakeProxy"

    def execute(self, context):
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        global theMessage, theErrorLines
        theErrorLines = theMessage.split('\n')
        maxlen = len(self.bl_label)
        for line in theErrorLines:
            if len(line) > maxlen:
                maxlen = len(line)
        width = 20+5*maxlen
        height = 20+5*len(theErrorLines)
        #self.report({'INFO'}, theMessage)
        wm = context.window_manager
        return wm.invoke_props_dialog(self, width=width, height=height)

    def draw(self, context):
        global theErrorLines
        for line in theErrorLines:
            self.layout.label(line)


class MHError(Exception):

    def __init__(self, value):
        global theMessage
        theMessage = value
        print("ERROR:", theMessage)
        bpy.ops.mhpxy.error('INVOKE_DEFAULT')

    def __str__(self):
        return repr(self.value)


def handleMHError(context):
    global theMessage

#
#   Warnings
#

_Warnings = []

def initWarnings():
    global _Warnings
    _Warnings = []

def handleWarnings():
    global _Warnings
    if _Warnings:
        string = "Operation succeeded but there were warnings:\n"
        for warning in _Warnings:
            string += "\n" + warning
        #raise MHError(string)

def addWarning(string):
    global _Warnings
    _Warnings.append(string)
