# Download images
# import os
# import requests
# from urllib.parse import urlsplit
# from os.path import basename

# book_urls = [
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book10.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book02.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book03.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book04.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book05.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book06.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book07.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book08.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book09.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book01.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book11.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book13.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book12.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book14.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book15.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book16.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book17.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book18.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book19.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book20.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book21.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book22.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book23.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book24.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book25.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book26.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book27.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book28.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book29.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book30.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book31.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book32.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book33.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book34.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book10.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book02.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book03.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book04.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book05.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book06.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book07.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book08.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book09.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book01.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book11.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book13.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book12.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book14.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book15.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book16.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book17.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book18.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book19.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book20.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book21.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book22.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book23.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book24.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book25.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book26.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book27.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book28.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book29.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book30.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book31.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book32.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book33.jpg",
#     "https://s3-us-west-2.amazonaws.com/s.cdpn.io/881020/book34.jpg",
# ]

# # Folder name where images will be saved
# folder_name = "cover_images"

# # Create the folder if it doesn't exist
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)

# # Function to download and save images
# def download_images(urls):
#     for idx, url in enumerate(urls):
#         try:
#             # Fetch image content from URL
#             response = requests.get(url)
#             response.raise_for_status()  # Raise an error for bad status codes
            
#             # Get the filename from the URL (or use a counter as fallback)
#             file_name = basename(urlsplit(url).path)
#             if not file_name:  # If there's no filename in URL, create one
#                 file_name = f"image_{idx + 1}.jpg"
            
#             # Full path to save the image
#             file_path = os.path.join(folder_name, file_name)
            
#             # Save the image to the folder
#             with open(file_path, 'wb') as file:
#                 file.write(response.content)
            
#             print(f"Downloaded: {file_name}")
        
#         except requests.exceptions.RequestException as e:
#             print(f"Failed to download {url}: {e}")

# # Call the function to download images
# download_images(book_urls)


# List files
# import os

# # Directory path (you can replace this with the path of your directory)
# directory = "cover_images"

# # List all files in the directory
# file_list = os.listdir(directory)

# # Print file names
# for file_name in file_list:
#     print(file_name)


# rename files to have more info
# import os
# import shutil

# # List of new file names based on your updated instructions
# new_file_names = [
#     "all_the_crooked_saints_by_maggie_stiefvater_genre_FTSY_published_on_10_October_2017_isbn_9780545930802_pages_320",
#     "and_then_there_were_none_by_agatha_christie_genre_MYST_THRILL_published_on_6_November_1939_isbn_9780062073488_pages_272",
#     "black_dog_by_caitlin_kittredge_genre_HORROR_published_on_9_September_2009_isbn_9780312943637_pages_365",
#     "der_kreide_mann_by_c_j_tudor_genre_MYST_THRILL_published_on_9_January_2018_isbn_9781524760997_pages_288",
#     "i_dont_cry_murder_by_jake_patterson_genre_MYST_THRILL_published_on_12_June_2011_isbn_9780980234077_pages_310",
#     "juniper_unraveling_by_keri_lake_genre_DYST_published_on_1_October_2017_isbn_9781947726032_pages_450",
#     "little_red_riding_hood_by_jack_zipes_genre_FTSY_published_on_15_August_1993_isbn_9780415908351_pages_128",
#     "magicians_impossible_by_brad_abraham_genre_FTSY_published_on_12_September_2017_isbn_9781250083521_pages_400",
#     "manhattan_by_woody_allen_genre_BIO_AUTOBIO_published_on_25_February_1979_isbn_9780345284321_pages_225",
#     "not_a_sound_by_heather_gudenkauf_genre_MYST_THRILL_published_on_30_May_2017_isbn_9780778319955_pages_352",
#     "one_perfect_day_by_rebecca_mead_genre_BIO_AUTOBIO_published_on_8_May_2008_isbn_9781596913560_pages_256",
#     "point_of_control_by_drake_green_genre_MYST_THRILL_published_on_7_March_2016_isbn_9781523855809_pages_280",
#     "resistance_by_barry_lopez_genre_HIST_FIC_published_on_4_March_2004_isbn_9781400030707_pages_240",
#     "spindle_fire_by_lexa_hillyer_genre_FTSY_published_on_11_April_2017_isbn_9780062440877_pages_368",
#     "the_art_of_crash_landing_by_melissa_decarlo_genre_FTSY_published_on_8_September_2015_isbn_9780062390547_pages_336",
#     "the_catastrophist_by_lawrence_eduglas_genre_HIST_FIC_published_on_1_January_2007_isbn_9780061451652_pages_320",
#     "the_death_of_bees_by_lisa_o_donnell_genre_HIST_FIC_published_on_2_January_2013_isbn_9780062209856_pages_336",
#     "the_elephant_vanishes_by_haruki_murakami_genre_FTSY_published_on_3_June_1993_isbn_9780679750536_pages_327",
#     "the_flame_alphabet_by_ben_marcus_genre_DYST_published_on_17_January_2012_isbn_9780307379375_pages_289",
#     "the_gone_world_by_tom_sweterlitsch_genre_SCIFI_published_on_6_February_2018_isbn_9780425278901_pages_400",
#     "the_great_gatsby_by_f_scott_fitzgerald_genre_HIST_FIC_published_on_10_April_1925_isbn_9780743273565_pages_180",
#     "the_inexplicables_by_cherie_priest_genre_FTSY_published_on_13_November_2012_isbn_9780765329487_pages_368",
#     "the_light_between_oceans_by_m_l_stedmax_genre_HIST_FIC_published_on_23_July_2012_isbn_9781451681734_pages_343",
#     "the_long_drop_by_denise_mina_genre_MYST_THRILL_published_on_2_March_2017_isbn_9781409150628_pages_240",
#     "the_nowhere_girls_by_amy_reed_genre_HIST_FIC_published_on_10_October_2017_isbn_9781481481731_pages_408",
#     "the_psychopath_test_by_jon_ronson_genre_BIO_AUTOBIO_published_on_12_May_2011_isbn_9781594485754_pages_288",
#     "the_queen_of_hearts_by_kimmery_martin_genre_ROM_published_on_13_February_2018_isbn_9780399585050_pages_352",
#     "the_sisters_brothers_by_patrick_dewitt_genre_HIST_FIC_published_on_15_April_2011_isbn_9780062041265_pages_325",
#     "the_snow_child_by_eowyn_ivey_genre_HIST_FIC_published_on_1_February_2012_isbn_9780316175676_pages_389",
#     "the_toy_collector_by_james_gunn_genre_HIST_FIC_published_on_13_February_2001_isbn_9781582341344_pages_278",
#     "the_tragedy_paper_by_elizabeth_laban_genre_HIST_FIC_published_on_8_January_2013_isbn_9780375870408_pages_320",
#     "the_unlikely_pilgrimage_of_harold_fry_by_rachel_joyce_genre_HIST_FIC_published_on_26_July_2012_isbn_9780812993295_pages_336",
#     "wink_poppy_midnight_by_april_genevieve_genre_FTSY_published_on_22_March_2016_isbn_9780803740488_pages_256",
#     "wonderful_world_by_javier_calvo_genre_HIST_FIC_published_on_5_November_2010_isbn_9788481097111_pages_340",
# ]

# # Directories for source and target
# source_dir = "cover_images"
# target_dir = "book_cover_pictures"

# # Create the target directory if it doesn't exist
# if not os.path.exists(target_dir):
#     os.makedirs(target_dir)

# # Function to copy and rename files
# def copy_and_rename_images():
#     for new_name in new_file_names:
#         # Extract the original title_by_author part from the new file name
#         original_name_part = "_".join(new_name.split("_")[:5])  # This gets 'title_by_author'

#         # Find the original file in the source directory
#         original_file = None
#         for file in os.listdir(source_dir):
#             if file.startswith(original_name_part):
#                 original_file = file
#                 break
        
#         if original_file:
#             # Full path to original and new file
#             original_path = os.path.join(source_dir, original_file)
#             new_path = os.path.join(target_dir, new_name + os.path.splitext(original_file)[1])  # Keep the same extension

#             # Copy and rename the file
#             shutil.copyfile(original_path, new_path)
#             print(f"Copied and renamed: {original_file} -> {new_name}")

# # Run the function
# copy_and_rename_images()

# Generate the string for creating instances
population_code = "from django.core.files import File\nfrom review.models import Author\nfrom review.models import Book, GenreChoices\n\n"

# Generate Author Instances population code
authors_info = {
    "maggie_stiefvater": {
        "first_name": "Maggie",
        "last_name": "Stiefvater",
        "bio": "Maggie Stiefvater is an American writer of young adult fiction. She is best known for her fantasy series such as 'The Raven Cycle' and 'Shiver', blending themes of myth, magic, and character-driven plots.",
        "year_of_birth": "1981-11-18"
    },
    "agatha_christie": {
        "first_name": "Agatha",
        "last_name": "Christie",
        "bio": "Agatha Christie, known as the 'Queen of Crime', was a prolific English writer. She created iconic detectives like Hercule Poirot and Miss Marple, and her works have become cornerstones of the mystery genre.",
        "year_of_birth": "1890-09-15"
    },
    "caitlin_kittredge": {
        "first_name": "Caitlin",
        "last_name": "Kittredge",
        "bio": "Caitlin Kittredge is an American author known for her urban fantasy and steampunk novels. Her works often explore dark, gritty themes, blending magic with complex, morally ambiguous characters.",
        "year_of_birth": "1984-09-02"
    },
    "c_j_tudor": {
        "first_name": "C.J.",
        "last_name": "Tudor",
        "bio": "C.J. Tudor is a British thriller writer whose debut novel, 'The Chalk Man', gained widespread acclaim. She is known for crafting suspenseful psychological thrillers that delve into dark and mysterious worlds.",
        "year_of_birth": "1972-06-26"
    },
    "jake_patterson": {
        "first_name": "Jake",
        "last_name": "Patterson",
        "bio": "Jake Patterson is an American thriller writer. He gained popularity for his gripping and suspenseful crime novels, which often feature complex protagonists embroiled in intricate murder mysteries.",
        "year_of_birth": "1975-04-10"
    },
    "keri_lake": {
        "first_name": "Keri",
        "last_name": "Lake",
        "bio": "Keri Lake is a bestselling author known for her dark romance and dystopian fantasy novels. Her work often explores post-apocalyptic worlds, combining strong emotional narratives with thrilling action.",
        "year_of_birth": "1980-11-12"
    },
    "jack_zipes": {
        "first_name": "Jack",
        "last_name": "Zipes",
        "bio": "Jack Zipes is a renowned folklorist and author. His expertise in fairy tales has made him one of the foremost scholars in his field. He is particularly known for analyzing the societal implications of folklore and children's literature.",
        "year_of_birth": "1937-12-07"
    },
    "brad_abraham": {
        "first_name": "Brad",
        "last_name": "Abraham",
        "bio": "Brad Abraham is a Canadian author and screenwriter. His debut novel 'Magicians Impossible' blends elements of urban fantasy and spy thriller, showcasing his versatility in storytelling.",
        "year_of_birth": "1974-02-15"
    },
    "woody_allen": {
        "first_name": "Woody",
        "last_name": "Allen",
        "bio": "Woody Allen is an American filmmaker, writer, and comedian. Known for his wit and neurotic style, he has created numerous critically acclaimed films, often focusing on existential themes and human relationships.",
        "year_of_birth": "1935-12-01"
    },
    "heather_gudenkauf": {
        "first_name": "Heather",
        "last_name": "Gudenkauf",
        "bio": "Heather Gudenkauf is a bestselling American author of mystery and suspense novels. Her works often focus on small-town secrets, family dynamics, and emotional struggles, with a strong sense of place and atmosphere.",
        "year_of_birth": "1967-10-06"
    },
    "rebecca_mead": {
        "first_name": "Rebecca",
        "last_name": "Mead",
        "bio": "Rebecca Mead is a British-American author and journalist. Best known for her memoir 'My Life in Middlemarch', she blends personal narrative with literary analysis in her writing.",
        "year_of_birth": "1966-06-12"
    },
        "drake_green": {
        "first_name": "Drake",
        "last_name": "Green",
        "bio": "Drake Green is a contemporary American author known for his mystery thrillers. His works often focus on high-stakes situations involving espionage, government conspiracies, and psychological drama.",
        "year_of_birth": "1982-07-23"
    },
    "barry_lopez": {
        "first_name": "Barry",
        "last_name": "Lopez",
        "bio": "Barry Lopez was an American author and essayist whose works centered on natural history and environmental issues. His book 'Arctic Dreams' won the National Book Award and established him as a leading voice on wilderness and ethics.",
        "year_of_birth": "1945-01-06"
    },
    "lexa_hillyer": {
        "first_name": "Lexa",
        "last_name": "Hillyer",
        "bio": "Lexa Hillyer is a YA author and poet known for her fantasy novels that often explore themes of self-discovery, adventure, and complex female protagonists. She is also the co-founder of a successful publishing company.",
        "year_of_birth": "1982-06-18"
    },
    "melissa_decarlo": {
        "first_name": "Melissa",
        "last_name": "DeCarlo",
        "bio": "Melissa DeCarlo is an American novelist who gained recognition with her debut novel 'The Art of Crash Landing', which combines humor and heartache in a story about self-discovery and family secrets.",
        "year_of_birth": "1969-03-22"
    },
    "lawrence_eduglas": {
        "first_name": "Lawrence",
        "last_name": "Eduglas",
        "bio": "Lawrence Eduglas is an author known for his rich historical fiction novels. He brings a deep sense of time and place to his narratives, often focusing on human conflicts and the complexities of power.",
        "year_of_birth": "1973-05-14"
    },
    "lisa_o_donnell": {
        "first_name": "Lisa",
        "last_name": "O'Donnell",
        "bio": "Lisa O'Donnell is a Scottish author and screenwriter whose debut novel, 'The Death of Bees', won the Commonwealth Book Prize. She writes deeply affecting stories with a unique voice, often blending dark humor with serious themes.",
        "year_of_birth": "1972-09-22"
    },
    "haruki_murakami": {
        "first_name": "Haruki",
        "last_name": "Murakami",
        "bio": "Haruki Murakami is one of Japan's most celebrated contemporary authors, known for his surreal, dream-like novels that blend magical realism, philosophical musings, and deep emotional undertones. His works include 'Norwegian Wood' and 'Kafka on the Shore'.",
        "year_of_birth": "1949-01-12"
    },
    "ben_marcus": {
        "first_name": "Ben",
        "last_name": "Marcus",
        "bio": "Ben Marcus is an American author known for his experimental and speculative fiction. His works often challenge traditional narrative structures, exploring the intersections of language, memory, and human experience.",
        "year_of_birth": "1967-10-24"
    },
    "tom_sweterlitsch": {
        "first_name": "Tom",
        "last_name": "Sweterlitsch",
        "bio": "Tom Sweterlitsch is an American science fiction author whose debut novel 'The Gone World' is known for its blend of hard science fiction and thriller elements. He often explores dystopian futures and mind-bending time travel.",
        "year_of_birth": "1977-08-19"
    },
    "f_scott_fitzgerald": {
        "first_name": "F. Scott",
        "last_name": "Fitzgerald",
        "bio": "F. Scott Fitzgerald was an American novelist and one of the greatest writers of the 20th century. Best known for 'The Great Gatsby', his works captured the essence of the Jazz Age and explored themes of decadence, idealism, and excess.",
        "year_of_birth": "1896-09-24"
    },
    "cherie_priest": {
        "first_name": "Cherie",
        "last_name": "Priest",
        "bio": "Cherie Priest is an American author known for her steampunk and urban fantasy novels. Her book 'Boneshaker' became a cult favorite, and her works are celebrated for their inventive world-building and strong, complex characters.",
        "year_of_birth": "1975-07-30"
    },
    "m_l_stedman": {
        "first_name": "M.L.",
        "last_name": "Stedman",
        "bio": "M.L. Stedman is an Australian author whose debut novel 'The Light Between Oceans' became a bestseller and was adapted into a major motion picture. Her works often focus on moral dilemmas and emotional depth.",
        "year_of_birth": "1965-03-01"
    },
    "denise_mina": {
        "first_name": "Denise",
        "last_name": "Mina",
        "bio": "Denise Mina is a Scottish crime writer and playwright. Known for her dark and gritty novels, she often explores themes of poverty, power dynamics, and social justice through complex characters and morally challenging situations.",
        "year_of_birth": "1966-08-21"
    },
    "amy_reed": {
        "first_name": "Amy",
        "last_name": "Reed",
        "bio": "Amy Reed is an American YA author known for her emotionally intense novels that often deal with difficult topics such as mental illness, addiction, and identity. Her works are characterized by raw honesty and powerful storytelling.",
        "year_of_birth": "1975-11-03"
    },
    "jon_ronson": {
        "first_name": "Jon",
        "last_name": "Ronson",
        "bio": "Jon Ronson is a Welsh journalist and author known for his humorous and often bizarre explorations of the human mind and society. His bestselling book 'The Psychopath Test' is a fascinating look at mental illness and eccentricity.",
        "year_of_birth": "1967-05-10"
    },
    "kimmery_martin": {
        "first_name": "Kimmery",
        "last_name": "Martin",
        "bio": "Kimmery Martin is an American author and former emergency medicine physician. She writes contemporary fiction that often draws on her medical background, exploring the complexities of relationships and life in the medical field.",
        "year_of_birth": "1974-11-16"
    },
    "patrick_dewitt": {
        "first_name": "Patrick",
        "last_name": "deWitt",
        "bio": "Patrick deWitt is a Canadian author known for his quirky and darkly humorous novels. His works, such as 'The Sisters Brothers', often explore the absurdities of life through richly drawn characters and sharp dialogue.",
        "year_of_birth": "1975-03-22"
    },
    "eowyn_ivey": {
        "first_name": "Eowyn",
        "last_name": "Ivey",
        "bio": "Eowyn Ivey is an American author from Alaska whose debut novel 'The Snow Child' was a finalist for the Pulitzer Prize. Her work often draws on Alaskan wilderness and folklore, blending magical realism with vivid natural imagery.",
        "year_of_birth": "1973-06-15"
    },
    "james_gunn": {
        "first_name": "James",
        "last_name": "Gunn",
        "bio": "James Gunn is an American filmmaker, screenwriter, and author. Known for his work in both Hollywood and fiction writing, Gunn is recognized for his eclectic and often satirical works across genres, particularly in the realms of superhero films and sci-fi.",
        "year_of_birth": "1966-08-05"
    },
    "elizabeth_laban": {
        "first_name": "Elizabeth",
        "last_name": "Laban",
        "bio": "Elizabeth Laban is an American author known for her young adult novels. Her works often focus on relationships, academic life, and personal growth, with an emphasis on emotional intelligence and empathy.",
        "year_of_birth": "1975-09-19"
    },
    "rachel_joyce": {
        "first_name": "Rachel",
        "last_name": "Joyce",
        "bio": "Rachel Joyce is a British novelist and playwright best known for her debut novel 'The Unlikely Pilgrimage of Harold Fry'. Her works often explore themes of kindness, human connections, and the complexities of life through quirky, endearing characters.",
        "year_of_birth": "1962-11-20"
    },
    "april_genevieve": {
        "first_name": "April",
        "last_name": "Genevieve Tucholke",
        "bio": "April Genevieve Tucholke is an American YA author known for her gothic and atmospheric novels. Her writing is often dark and mysterious, blending elements of horror, fantasy, and romance.",
        "year_of_birth": "1982-12-08"
    },
    "javier_calvo": {
        "first_name": "Javier",
        "last_name": "Calvo",
        "bio": "Javier Calvo is a Spanish author and screenwriter known for his engaging young adult novels that often explore themes of identity, belonging, and personal growth. His writing is characterized by a blend of realism and magical elements.",
        "year_of_birth": "1982-03-30"
    },
}

for author_key, author_data in authors_info.items():
    creation_line = (
        f"{author_key}=Author.objects.create(first_name=\"{author_data['first_name']}\", "
        f"last_name=\"{author_data['last_name']}\", "
        f"bio=\"{author_data['bio']}\", "
        f"year_of_birth=\"{author_data['year_of_birth']}\")\n"
    )
    population_code += creation_line

population_code += "\n"

# Generate Book Instances population code
import os
directory = "book_cover_pictures"

# List all files in the directory
file_names = os.listdir(directory)

# Dictionary to map genre codes to actual genre choices
genre_mapping_str = """
class GenreChoices(models.TextChoices):
    FANTASY = "FTSY", "Fantasy"
    SCI_FI = "SCIFI", "Science Fiction"
    MYSTERY_THRILLER = "MYST_THRILL", "Mystery/Thriller"
    ROMANCE = "ROM", "Romance" 
    HISTORICAL_FICTION = "HIST_FIC", "Historical Fiction"
    HORROR = "HORROR", "Horror"
    DYSTOPIAN = "DYST", "Dystopian"
    ADVENTURE = "ADVN", "Adventure"
    BIO_AUTOBIO = "BIO_AUTOBIO", "Biography/Autobiography"
    SELF_HELP = "SELF_HELP", "Self Help"
    HISTORY = "HIST", "History"
    SCIENCE = "SCI", "Science"
    BUSINESS = "BSNS", "Business"
"""

# Initialize the genre mapping dictionary
genre_mapping = {}

# Split the enum string by lines
lines = genre_mapping_str.strip().split('\n')[1:]

# Loop through each line to extract code and genre
for line in lines:
    # Split by '=' to separate the enum key and value
    key, value = line.split('=')
    
    # Clean up the key (strip whitespace)
    key = key.strip()
    
    # Extract the genre code and description from the value
    genre_code, genre_name = value.split(',')
    
    # Clean up the genre code and name (strip quotes and whitespace)
    genre_code = genre_code.strip().replace('"', '')
    genre_name = genre_name.strip().replace('"', '')
    
    # Add to the genre_mapping dictionary
    genre_mapping[genre_code] = f"GenreChoices.{key}"


# Get the base path dynamically based on the current script's directory
base_path = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
cover_image_path = os.path.join(base_path, 'book_cover_pictures/')  # Append the subdirectory
cover_image_path = cover_image_path.replace('\\', '/')
print(cover_image_path)  # This will print the full path to the book_cover_pictures directory



for file_name in file_names:
    # Remove the file extension (.jpg)
    file_name_no_ext = os.path.splitext(file_name)[0]

    # Split the filename into parts based on underscores
    parts = file_name_no_ext.split('_')

    # Extract book title: everything before 'by'
    title_index = parts.index('by')
    title_parts = parts[:title_index]
    title = ' '.join(title_parts).title()

    # Extract author: everything between 'by' and 'genre'
    author_index = parts.index('genre')
    author_names = parts[title_index + 1:author_index]
    author_first_name = '_'.join(author_names[:-1])  # All but the last name
    author_last_name = author_names[-1]  # The last name
    author = f"{author_first_name.lower()}_{author_last_name.lower()}"

    # Extract genre: everything between 'genre' and 'published'
    genre_index = parts.index('published')
    genre_code = "_".join(parts[author_index+1:genre_index])
    genre = genre_mapping.get(genre_code, 'GenreChoices.MYSTERY_THRILLER')  # Default if not found

    # Dictionary to map full month names to numeric values
    month_mapping = {
        "January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06",
        "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"
    }

    # Extract publication date: everything between 'on' and 'isbn'
    publication_day = parts[genre_index + 2]
    publication_month_text = parts[genre_index + 3]  # Use the full month name
    publication_year = parts[genre_index + 4]

    # Convert full month name to numeric value using the month_mapping dictionary
    publication_month = month_mapping.get(publication_month_text, "01")  # Default to "01" if not found

    # Format the publication date in YYYY-MM-DD format
    publication_date = f"{publication_year}-{publication_month}-{publication_day.zfill(2)}"  # Format: YYYY-MM-DD


    # Extract ISBN: everything between 'isbn' and 'pages'
    isbn_index = parts.index('isbn')
    isbn = parts[isbn_index + 1]

    # Extract number of pages: the last part in the filename
    number_of_pages = parts[-1]

    # Construct the cover image path
    cover_image = f"{cover_image_path}{file_name}"

    # Generate the Book creation line if the author is known
    creation_line = (
        f"image_path = '{cover_image}'\n"
        "with open(image_path, 'rb') as image_file:\n"
        "    image_file_obj = File(image_file)\n"
        f"    Book.objects.create(title='{title}', "
        f"author={author}, "
        f"genre={genre}, "
        f"publication_date='{publication_date}', "
        f"cover_image=image_file_obj, "
        f"isbn='{isbn}', "
        f"number_of_pages={number_of_pages})\n\n"
    )
    population_code += creation_line

# Export the generated code
with open("populate_db.py", "w") as f:
    f.write(population_code)
