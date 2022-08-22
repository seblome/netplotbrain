

def _add_subplot_title(ax, azim=None, elev=None, subtitle_frame='auto', hemisphere='both', viewtype='b', **kwargs):
    subtitlefont = kwargs.get('font')
    subtitlecolor = kwargs.get('fontcolor')
    subtitlefontsize = kwargs.get('subtitlefontsize')
    subtitleloc = kwargs.get('subtitleloc')
    subtitleweight = kwargs.get('subtitleweight')
    if subtitle_frame == 'auto':
        viewcoord = (azim, elev)
        subtitle_frame = ''
        if viewcoord == (180, 10):
            subtitle_frame = 'Left'
        elif viewcoord == (0, 10):
            subtitle_frame = 'Right'
        elif viewcoord == (90, 10):
            subtitle_frame = 'Anterior'
        elif viewcoord == (-90, 10):
            subtitle_frame = 'Posterior'
        elif viewcoord == (-90, 90) and viewtype == 'b':
            subtitle_frame = 'Superior'
        elif viewcoord == (90, 90):
            subtitle_frame = 'Inferior'
        # Add hemisphere
        if hemisphere == 'L' or hemisphere == 'left':
            subtitle_frame += ' (left hemisphere)'
        elif hemisphere == 'R' or hemisphere == 'right':
            subtitle_frame += ' (right hemisphere)'

    ax.set_title(subtitle_frame, fontname=subtitlefont,
                     fontweight=subtitleweight, color=subtitlecolor,
                     fontsize=subtitlefontsize,
                     loc=subtitleloc)
    


def _add_title(fig, **kwargs):
    title = kwargs.get('title')
    titlefont = kwargs.get('font')
    titlecolor = kwargs.get('fontcolor')
    titlefontsize = kwargs.get('titlefontsize')
    titleweight = kwargs.get('titleweight')
        
    fig.suptitle(title, fontname=titlefont,
                     fontweight=titleweight, 
                     color=titlecolor,
                     fontsize=titlefontsize)
    