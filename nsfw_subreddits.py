from utils.color_logger import *

anal_subreddits = ['AnalGW', 'anal', 'AnalOrgasms', 'anal_gifs']

hardcore_subreddits = ['HardcoreNSFW', 'nsfw', 'NSFW_HardGifs', 'NSFW_hardcore', 'nsfwhardcore']

hentai_subreddits = ['hentai', 'HENTAI_GIF', 'MonsterGirl', 'PokePorn', 'NSFWgaming', 'hentaibondage', 'thick_hentai',
                     'BokuNoEroAcademia']

blowjob_subreddits = ['BlowJob', 'IWantToSuckCock', 'FaceFuck']

boobies_subreddits = ['boobs', 'treesgonewild', 'hugeboobs', 'BigBoobsGonewild']

nsfw_wtf_subreddits = ['nsfw_wtf']

fap_subreddits = ['NSFWgaming']

cosplay_subreddits = ['nsfwcosplay']

webcam_subreddits = ['CamSluts']

toys_subreddits = []

threesome_subreddits = []

tattoo_subreddits = []

striptease_subreddits = []

squirt_subreddits = []

russian_subreddits = []

rough_subreddits = []

pornstar_subreddits = []

porn_subreddits = ['SexInFrontOfOthers', 'RedheadGifs', 'LegalTeens', 'Amateur', 'FlashingGirls'] + \
                  pornstar_subreddits + rough_subreddits + russian_subreddits + squirt_subreddits + \
                  striptease_subreddits + tattoo_subreddits + threesome_subreddits + anal_subreddits + \
                  hardcore_subreddits + blowjob_subreddits + webcam_subreddits + toys_subreddits  # + hentai_subreddits + nsfw_wtf_subreddits

logger = colorlog.getLogger("NSFW_SUBREDDITS")

nsfw_subreddits = {
    "anal": ['AnalGW', 'anal', 'AnalOrgasms', 'anal_gifs'],
    "hardcore": ['HardcoreNSFW', 'nsfw', 'NSFW_HardGifs', 'NSFW_hardcore', 'nsfwhardcore'],
    "hentai": ['hentai', 'HENTAI_GIF', 'MonsterGirl', 'PokePorn', 'NSFWgaming', 'hentaibondage', 'thick_hentai',
               'BokuNoEroAcademia'],
    "blowjob": ['BlowJob', 'IWantToSuckCock', 'FaceFuck'],
    "boobies": ['boobs', 'treesgonewild', 'hugeboobs', 'BigBoobsGonewild'],
    "wtf": ['nsfw_wtf'],
    "fap": ['NSFWgaming'],
    "cosplay": ['nsfwcosplay'],
    "webcam": ['CamSluts'],
    "toys": [],
    "threesome": [],
    "tattoo": [],
    "striptease": [],
    "squirt": [],
    "russian": [],
}
nsfw_subreddits["pornstar"] = nsfw_subreddits.get('webcam')
nsfw_subreddits["porn"] = [item for key, _list in nsfw_subreddits.items() if key != 'wtf' and key != 'hentai' for item in _list] + ['SexInFrontOfOthers', 'RedheadGifs', 'LegalTeens', 'Amateur', 'FlashingGirls']

logger.info("{}".format(nsfw_subreddits.get('porn')))

def choose_porn_subreddits(query):
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
    if query == 'porn':
        return nsfw_subreddits.get('porn')
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
    # TODO ADD MORE LISTS
    return nsfw_subreddits['porn']
