r"""
存放一些CSS格式常量，当然也可以直接在ui里面改，但是这样方便写，有时也可实现动态效果
"""

HORIZONTAL_SCOLLBAR_STYLE = '''
QScrollBar:horizontal
{
    height:14px;
    background:rgba(176, 196, 234,0%);
    margin:0px,0px,0px,0px;
    padding-left:15px;  
    padding-right:15px;
}
QScrollBar::handle:horizontal
{
    height:14px;
    background:rgba(176, 196, 234,25%);
    border-radius:4px;  
    min-width:20;
}
QScrollBar::handle:horizontal:hover
{
    height:14px;
    background:rgba(176, 196, 234,50%); 
    border-radius:4px;
    min-width:20;
}

QScrollBar::add-line:horizontal
{
    height:14px;width:14px;
    border-image:url(:/imgs/arrow_right_blue.png);
    
    subcontrol-position:right;
}
QScrollBar::sub-line:horizontal 
{
    height:14px;width:14px;
    border-image:url(:/imgs/arrow_left_blue.png);
    subcontrol-position:left;
}
QScrollBar::add-line:horizontal:hover  
{
    height:14px;width:14px;
    border-image:url(:/imgs/arrow_right.png);
    subcontrol-position:right;
}
QScrollBar::sub-line:horizontal:hover  
{
    height:14px;width:14px;
    border-image:url(:/imgs/arrow_left.png);
    subcontrol-position:left;
}
QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal
{
    background:rgba(176, 196, 234,10%);
}
'''

VERTICAL_SCOLLBAR_STYLE = '''
QScrollBar:vertical
{
    width:14px;
    background:rgba(176, 196, 234,0%);
    margin:0px,0px,0px,0px;
    padding-top:15px;  
    padding-bottom:15px;
}
QScrollBar::handle:vertical
{
    width:14px;
    background:rgba(176, 196, 234,25%);
    border-radius:4px;  
    min-height:20;
}
QScrollBar::handle:vertical:hover
{
    width:14px;
    background:rgba(176, 196, 234,50%); 
    border-radius:4px;
    min-height:20;
}

QScrollBar::add-line:vertical 
{
    height:14px;width:14px;
    border-image:url(:/imgs/arrow_down_blue.png);
    
    subcontrol-position:bottom;
}
QScrollBar::sub-line:vertical  
{
    height:14px;width:14px;
    border-image:url(:/imgs/arrow_up_blue.png);
    subcontrol-position:top;
}
QScrollBar::add-line:vertical:hover  
{
    height:14px;width:14px;
    border-image:url(:/imgs/arrow_down.png);
    subcontrol-position:bottom;
}
QScrollBar::sub-line:vertical:hover  
{
    height:14px;width:14px;
    border-image:url(:/imgs/arrow_up.png);
    subcontrol-position:top;
}
QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical  
{
    background:rgba(176, 196, 234,10%);
}
'''
