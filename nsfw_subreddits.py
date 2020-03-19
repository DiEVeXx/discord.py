query = None

anal_subreddits = ['AnalGW', 'anal', 'AnalOrgasms', 'anal_gifs']

hardcore_subreddits = ['HardcoreNSFW', 'nsfw', 'NSFW_HardGifs', 'NSFW_hardcore', 'nsfwhardcore']

hentai_subreddits = ['hentai', 'HENTAI_GIF', 'MonsterGirl', 'PokePorn', 'NSFWgaming', 'hentaibondage', 'thick_hentai',
                     'BokuNoEroAcademia']

blowjob_subreddits = ['BlowJob', 'IWantToSuckCock', 'SexInFrontOfOthers', 'RedheadGifs', 'FaceFuck']

webcam_subreddits = []

toys_subreddits = []

threesome_subreddits = []

tattoo_subreddits = []

striptease_subreddits = []

squirt_subreddits = []

russian_subreddits = []

rough_subreddits = []

pornstar_subreddits = []

parody_subreddits = []

porn_subreddits = parody_subreddits + pornstar_subreddits + rough_subreddits + russian_subreddits + squirt_subreddits + striptease_subreddits + tattoo_subreddits + threesome_subreddits + anal_subreddits + hardcore_subreddits + blowjob_subreddits + webcam_subreddits + toys_subreddits  # + hentai_subreddits

fap_subreddits = ['NSFWgaming']


def choose_porn_subreddits(query):
    if query == 'anal':
        return anal_subreddits
    if query == 'porn':
        return porn_subreddits
    if query == 'fap':
        return fap_subreddits
    if query == 'hentai':
        return hentai_subreddits
    # TODO ADD MORE LISTS
    return porn_subreddits
