from utils.color_logger import *

logger = colorlog.getLogger("NSFW_SUBREDDITS")

nsfw_subreddits = {
    "anal": ['AnalPorn', 'AnalGW', 'anal', 'AnalOrgasms', 'anal_gifs', 'AnalVidz', 'Anal_Babes', 'Anal_witch', 'buttsex'],
    "hardcore": ['HardcoreNSFW', 'nsfw', 'NSFW_HardGifs', 'NSFW_hardcore', 'nsfwhardcore', 'distension', 'Pushing'],
    "hentai": ['hentai', 'HENTAI_GIF', 'MonsterGirl', 'PokePorn', 'NSFWgaming', 'hentaibondage', 'thick_hentai',
               'BokuNoEroAcademia'],
    "blowjob": ['BlowjobEyeContact', 'OnHerKnees', 'Blowjobs', 'BlowJob', 'IWantToSuckCock', 'FaceFuck', 'Gloryholes'],
    "boobies": ['motiontrackedboobs', 'boobs', 'treesgonewild', 'hugeboobs', 'NoTop', 'Topless_Vixens'],
    "facial": ['FacialFun', 'Facials'],
    "wtf": ['nsfw_wtf'],
    "fap": ['NSFWgaming', 'DirtyGaming', 'girlsdoingnerdythings', ''],
    "cosplay": ['nsfwcosplay', 'cosplayonoff', 'Cosporn', 'CosplayBoobs', 'cat_girls', 'GirlswithNeonHair'],
    "webcam": ['CamSluts'],
    "ass": ['ass', 'OiledAss'],
    "milf": ['milfcumsluts'],
    "nudes": ['holdthemoan'],
    "toys": [],
    "threesome": [],
    "tattoo": [],
    "striptease": [],
    "squirt": ['squirting', 'GushingGirls'],
    "russian": [],
}

nsfw_subreddits["pornstar"] = nsfw_subreddits.get('webcam') + ['ttaylorwhite', 'PornStars', ]
nsfw_subreddits["porn"] = [item for key, _list in nsfw_subreddits.items() if
                           key not in ['wtf', 'hentai', 'fap', 'cosplay', 'boobies'] for item in _list] + \
                          ['nsfwHTML5', 'sexgifs', 'porngif', 'Penetration_gifs', 'porninfifteenseconds', 'NSFW_GFY',
                           'nsfwgif', 'PornGifs', 'XXX_Animated_Gifs', 'adultgifs', 'porn_gifs', 'NSFW_HTML5',
                           '60fpsporn', 'carnalclass', 'nsfw_gifs', 'NSFW_GIF', 'SexInFrontOfOthers', 'RedheadGifs',
                           'Amateur', 'FlashingGirls', 'Oilporn', 'The_Best_NSFW_GIFS']  # 'LegalTeens'


def choose_nsfw_subreddits(query):
    """
    returns a list of nsfw subreddits
    Parameters
    ----------
    query

    Returns
    -------
    a list of strings
    """
    if query == 'anal':
        return nsfw_subreddits.get('anal')
    if query == 'hardcore':
        return nsfw_subreddits.get('hardcore')
    if query == 'fap':
        return nsfw_subreddits.get('fap')
    if query == 'hentai':
        return nsfw_subreddits.get('hentai')
    if query == 'cosplay':
        return nsfw_subreddits.get('cosplay')
    if query == 'boobies' or query == 'boobs' or query == 'tetas':
        return nsfw_subreddits.get('boobies')
    if query == 'blowjob':
        return nsfw_subreddits.get('blowjob')
    if query == 'wtf':
        return nsfw_subreddits.get('wtf')
    if query == 'webcam':
        return nsfw_subreddits.get('webcam')
    if query == 'squirt':
        return nsfw_subreddits.get('squirt')
    if query == 'facial':
        return nsfw_subreddits.get('facial')
    if query == 'pornstar':
        return nsfw_subreddits.get('pornstar')
    if query == 'nudes':
        return nsfw_subreddits.get('nudes')
    if query == 'milf':
        return nsfw_subreddits.get('milf')
    # TODO ADD MORE LISTS
    return nsfw_subreddits['porn']
