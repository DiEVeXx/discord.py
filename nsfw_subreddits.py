query = None

anal_subreddits = ['AnalGW', 'anal', 'AnalOrgasms', 'anal_gifs']

hardcore_subreddits = ['HardcoreNSFW', 'nsfw', 'NSFW_HardGifs', 'NSFW_hardcore', 'nsfwhardcore']

hentai_subreddits = ['hentai', 'HENTAI_GIF', 'MonsterGirl', 'PokePorn', 'NSFWgaming', 'hentaibondage', 'thick_hentai',
                     'BokuNoEroAcademia']

blowjob_subreddits = ['BlowJob', 'IWantToSuckCock', 'FaceFuck']

boobies_subreddits = ['boobs', 'treesgonewild', 'hugeboobs', 'BigBoobsGonewild']

parody_subreddits = ['nsfw_wtf']

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

porn_subreddits = ['SexInFrontOfOthers', 'RedheadGifs', 'LegalTeens', 'Amateur', 'FlashingGirls'] + parody_subreddits + \
                  pornstar_subreddits + rough_subreddits + russian_subreddits + squirt_subreddits + \
                  striptease_subreddits + tattoo_subreddits + threesome_subreddits + anal_subreddits + \
                  hardcore_subreddits + blowjob_subreddits + webcam_subreddits + toys_subreddits  # + hentai_subreddits


def choose_porn_subreddits(query):
    if query == 'anal':
        return anal_subreddits
    if query == 'porn':
        return porn_subreddits
    if query == 'fap':
        return fap_subreddits
    if query == 'hentai':
        return hentai_subreddits
    if query == 'cosplay':
        return cosplay_subreddits
    if query == 'boobies' or query == 'boobs' or query == 'tetas':
        return boobies_subreddits
    if query == 'blowjob':
        return blowjob_subreddits
    if query == 'wtf':
        return parody_subreddits
    if query == 'webcam':
        return webcam_subreddits
    # TODO ADD MORE LISTS
    return porn_subreddits
