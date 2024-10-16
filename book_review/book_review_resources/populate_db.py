from django.core.files import File
from review.models import Author
from review.models import Book, GenreChoices

maggie_stiefvater=Author.objects.create(first_name="Maggie", last_name="Stiefvater", bio="Maggie Stiefvater is an American writer of young adult fiction. She is best known for her fantasy series such as 'The Raven Cycle' and 'Shiver', blending themes of myth, magic, and character-driven plots.", year_of_birth="1981-11-18")
agatha_christie=Author.objects.create(first_name="Agatha", last_name="Christie", bio="Agatha Christie, known as the 'Queen of Crime', was a prolific English writer. She created iconic detectives like Hercule Poirot and Miss Marple, and her works have become cornerstones of the mystery genre.", year_of_birth="1890-09-15")
caitlin_kittredge=Author.objects.create(first_name="Caitlin", last_name="Kittredge", bio="Caitlin Kittredge is an American author known for her urban fantasy and steampunk novels. Her works often explore dark, gritty themes, blending magic with complex, morally ambiguous characters.", year_of_birth="1984-09-02")
c_j_tudor=Author.objects.create(first_name="C.J.", last_name="Tudor", bio="C.J. Tudor is a British thriller writer whose debut novel, 'The Chalk Man', gained widespread acclaim. She is known for crafting suspenseful psychological thrillers that delve into dark and mysterious worlds.", year_of_birth="1972-06-26")
jake_patterson=Author.objects.create(first_name="Jake", last_name="Patterson", bio="Jake Patterson is an American thriller writer. He gained popularity for his gripping and suspenseful crime novels, which often feature complex protagonists embroiled in intricate murder mysteries.", year_of_birth="1975-04-10")
keri_lake=Author.objects.create(first_name="Keri", last_name="Lake", bio="Keri Lake is a bestselling author known for her dark romance and dystopian fantasy novels. Her work often explores post-apocalyptic worlds, combining strong emotional narratives with thrilling action.", year_of_birth="1980-11-12")
jack_zipes=Author.objects.create(first_name="Jack", last_name="Zipes", bio="Jack Zipes is a renowned folklorist and author. His expertise in fairy tales has made him one of the foremost scholars in his field. He is particularly known for analyzing the societal implications of folklore and children's literature.", year_of_birth="1937-12-07")
brad_abraham=Author.objects.create(first_name="Brad", last_name="Abraham", bio="Brad Abraham is a Canadian author and screenwriter. His debut novel 'Magicians Impossible' blends elements of urban fantasy and spy thriller, showcasing his versatility in storytelling.", year_of_birth="1974-02-15")
woody_allen=Author.objects.create(first_name="Woody", last_name="Allen", bio="Woody Allen is an American filmmaker, writer, and comedian. Known for his wit and neurotic style, he has created numerous critically acclaimed films, often focusing on existential themes and human relationships.", year_of_birth="1935-12-01")
heather_gudenkauf=Author.objects.create(first_name="Heather", last_name="Gudenkauf", bio="Heather Gudenkauf is a bestselling American author of mystery and suspense novels. Her works often focus on small-town secrets, family dynamics, and emotional struggles, with a strong sense of place and atmosphere.", year_of_birth="1967-10-06")
rebecca_mead=Author.objects.create(first_name="Rebecca", last_name="Mead", bio="Rebecca Mead is a British-American author and journalist. Best known for her memoir 'My Life in Middlemarch', she blends personal narrative with literary analysis in her writing.", year_of_birth="1966-06-12")
drake_green=Author.objects.create(first_name="Drake", last_name="Green", bio="Drake Green is a contemporary American author known for his mystery thrillers. His works often focus on high-stakes situations involving espionage, government conspiracies, and psychological drama.", year_of_birth="1982-07-23")
barry_lopez=Author.objects.create(first_name="Barry", last_name="Lopez", bio="Barry Lopez was an American author and essayist whose works centered on natural history and environmental issues. His book 'Arctic Dreams' won the National Book Award and established him as a leading voice on wilderness and ethics.", year_of_birth="1945-01-06")
lexa_hillyer=Author.objects.create(first_name="Lexa", last_name="Hillyer", bio="Lexa Hillyer is a YA author and poet known for her fantasy novels that often explore themes of self-discovery, adventure, and complex female protagonists. She is also the co-founder of a successful publishing company.", year_of_birth="1982-06-18")
melissa_decarlo=Author.objects.create(first_name="Melissa", last_name="DeCarlo", bio="Melissa DeCarlo is an American novelist who gained recognition with her debut novel 'The Art of Crash Landing', which combines humor and heartache in a story about self-discovery and family secrets.", year_of_birth="1969-03-22")
lawrence_eduglas=Author.objects.create(first_name="Lawrence", last_name="Eduglas", bio="Lawrence Eduglas is an author known for his rich historical fiction novels. He brings a deep sense of time and place to his narratives, often focusing on human conflicts and the complexities of power.", year_of_birth="1973-05-14")
lisa_o_donnell=Author.objects.create(first_name="Lisa", last_name="O'Donnell", bio="Lisa O'Donnell is a Scottish author and screenwriter whose debut novel, 'The Death of Bees', won the Commonwealth Book Prize. She writes deeply affecting stories with a unique voice, often blending dark humor with serious themes.", year_of_birth="1972-09-22")
haruki_murakami=Author.objects.create(first_name="Haruki", last_name="Murakami", bio="Haruki Murakami is one of Japan's most celebrated contemporary authors, known for his surreal, dream-like novels that blend magical realism, philosophical musings, and deep emotional undertones. His works include 'Norwegian Wood' and 'Kafka on the Shore'.", year_of_birth="1949-01-12")
ben_marcus=Author.objects.create(first_name="Ben", last_name="Marcus", bio="Ben Marcus is an American author known for his experimental and speculative fiction. His works often challenge traditional narrative structures, exploring the intersections of language, memory, and human experience.", year_of_birth="1967-10-24")
tom_sweterlitsch=Author.objects.create(first_name="Tom", last_name="Sweterlitsch", bio="Tom Sweterlitsch is an American science fiction author whose debut novel 'The Gone World' is known for its blend of hard science fiction and thriller elements. He often explores dystopian futures and mind-bending time travel.", year_of_birth="1977-08-19")
f_scott_fitzgerald=Author.objects.create(first_name="F. Scott", last_name="Fitzgerald", bio="F. Scott Fitzgerald was an American novelist and one of the greatest writers of the 20th century. Best known for 'The Great Gatsby', his works captured the essence of the Jazz Age and explored themes of decadence, idealism, and excess.", year_of_birth="1896-09-24")
cherie_priest=Author.objects.create(first_name="Cherie", last_name="Priest", bio="Cherie Priest is an American author known for her steampunk and urban fantasy novels. Her book 'Boneshaker' became a cult favorite, and her works are celebrated for their inventive world-building and strong, complex characters.", year_of_birth="1975-07-30")
m_l_stedman=Author.objects.create(first_name="M.L.", last_name="Stedman", bio="M.L. Stedman is an Australian author whose debut novel 'The Light Between Oceans' became a bestseller and was adapted into a major motion picture. Her works often focus on moral dilemmas and emotional depth.", year_of_birth="1965-03-01")
denise_mina=Author.objects.create(first_name="Denise", last_name="Mina", bio="Denise Mina is a Scottish crime writer and playwright. Known for her dark and gritty novels, she often explores themes of poverty, power dynamics, and social justice through complex characters and morally challenging situations.", year_of_birth="1966-08-21")
amy_reed=Author.objects.create(first_name="Amy", last_name="Reed", bio="Amy Reed is an American YA author known for her emotionally intense novels that often deal with difficult topics such as mental illness, addiction, and identity. Her works are characterized by raw honesty and powerful storytelling.", year_of_birth="1975-11-03")
jon_ronson=Author.objects.create(first_name="Jon", last_name="Ronson", bio="Jon Ronson is a Welsh journalist and author known for his humorous and often bizarre explorations of the human mind and society. His bestselling book 'The Psychopath Test' is a fascinating look at mental illness and eccentricity.", year_of_birth="1967-05-10")
kimmery_martin=Author.objects.create(first_name="Kimmery", last_name="Martin", bio="Kimmery Martin is an American author and former emergency medicine physician. She writes contemporary fiction that often draws on her medical background, exploring the complexities of relationships and life in the medical field.", year_of_birth="1974-11-16")
patrick_dewitt=Author.objects.create(first_name="Patrick", last_name="deWitt", bio="Patrick deWitt is a Canadian author known for his quirky and darkly humorous novels. His works, such as 'The Sisters Brothers', often explore the absurdities of life through richly drawn characters and sharp dialogue.", year_of_birth="1975-03-22")
eowyn_ivey=Author.objects.create(first_name="Eowyn", last_name="Ivey", bio="Eowyn Ivey is an American author from Alaska whose debut novel 'The Snow Child' was a finalist for the Pulitzer Prize. Her work often draws on Alaskan wilderness and folklore, blending magical realism with vivid natural imagery.", year_of_birth="1973-06-15")
james_gunn=Author.objects.create(first_name="James", last_name="Gunn", bio="James Gunn is an American filmmaker, screenwriter, and author. Known for his work in both Hollywood and fiction writing, Gunn is recognized for his eclectic and often satirical works across genres, particularly in the realms of superhero films and sci-fi.", year_of_birth="1966-08-05")
elizabeth_laban=Author.objects.create(first_name="Elizabeth", last_name="Laban", bio="Elizabeth Laban is an American author known for her young adult novels. Her works often focus on relationships, academic life, and personal growth, with an emphasis on emotional intelligence and empathy.", year_of_birth="1975-09-19")
rachel_joyce=Author.objects.create(first_name="Rachel", last_name="Joyce", bio="Rachel Joyce is a British novelist and playwright best known for her debut novel 'The Unlikely Pilgrimage of Harold Fry'. Her works often explore themes of kindness, human connections, and the complexities of life through quirky, endearing characters.", year_of_birth="1962-11-20")
april_genevieve=Author.objects.create(first_name="April", last_name="Genevieve Tucholke", bio="April Genevieve Tucholke is an American YA author known for her gothic and atmospheric novels. Her writing is often dark and mysterious, blending elements of horror, fantasy, and romance.", year_of_birth="1982-12-08")
javier_calvo=Author.objects.create(first_name="Javier", last_name="Calvo", bio="Javier Calvo is a Spanish author and screenwriter known for his engaging young adult novels that often explore themes of identity, belonging, and personal growth. His writing is characterized by a blend of realism and magical elements.", year_of_birth="1982-03-30")

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/all_the_crooked_saints_by_maggie_stiefvater_genre_FTSY_published_on_10_October_2017_isbn_9780545930802_pages_320.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='All The Crooked Saints', author=maggie_stiefvater, genre=GenreChoices.FANTASY, publication_date='2017-10-10', cover_image=image_file_obj, isbn='9780545930802', number_of_pages=320)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/and_then_there_were_none_by_agatha_christie_genre_MYST_THRILL_published_on_6_November_1939_isbn_9780062073488_pages_272.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='And Then There Were None', author=agatha_christie, genre=GenreChoices.MYSTERY_THRILLER, publication_date='1939-11-06', cover_image=image_file_obj, isbn='9780062073488', number_of_pages=272)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/black_dog_by_caitlin_kittredge_genre_HORROR_published_on_9_September_2009_isbn_9780312943637_pages_365.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='Black Dog', author=caitlin_kittredge, genre=GenreChoices.HORROR, publication_date='2009-09-09', cover_image=image_file_obj, isbn='9780312943637', number_of_pages=365)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/der_kreide_mann_by_c_j_tudor_genre_MYST_THRILL_published_on_9_January_2018_isbn_9781524760997_pages_288.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='Der Kreide Mann', author=c_j_tudor, genre=GenreChoices.MYSTERY_THRILLER, publication_date='2018-01-09', cover_image=image_file_obj, isbn='9781524760997', number_of_pages=288)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/i_dont_cry_murder_by_jake_patterson_genre_MYST_THRILL_published_on_12_June_2011_isbn_9780980234077_pages_310.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='I Dont Cry Murder', author=jake_patterson, genre=GenreChoices.MYSTERY_THRILLER, publication_date='2011-06-12', cover_image=image_file_obj, isbn='9780980234077', number_of_pages=310)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/juniper_unraveling_by_keri_lake_genre_DYST_published_on_1_October_2017_isbn_9781947726032_pages_450.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='Juniper Unraveling', author=keri_lake, genre=GenreChoices.DYSTOPIAN, publication_date='2017-10-01', cover_image=image_file_obj, isbn='9781947726032', number_of_pages=450)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/little_red_riding_hood_by_jack_zipes_genre_FTSY_published_on_15_August_1993_isbn_9780415908351_pages_128.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='Little Red Riding Hood', author=jack_zipes, genre=GenreChoices.FANTASY, publication_date='1993-08-15', cover_image=image_file_obj, isbn='9780415908351', number_of_pages=128)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/magicians_impossible_by_brad_abraham_genre_FTSY_published_on_12_September_2017_isbn_9781250083521_pages_400.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='Magicians Impossible', author=brad_abraham, genre=GenreChoices.FANTASY, publication_date='2017-09-12', cover_image=image_file_obj, isbn='9781250083521', number_of_pages=400)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/not_a_sound_by_heather_gudenkauf_genre_MYST_THRILL_published_on_30_May_2017_isbn_9780778319955_pages_352.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='Not A Sound', author=heather_gudenkauf, genre=GenreChoices.MYSTERY_THRILLER, publication_date='2017-05-30', cover_image=image_file_obj, isbn='9780778319955', number_of_pages=352)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/one_perfect_day_by_rebecca_mead_genre_BIO_AUTOBIO_published_on_8_May_2008_isbn_9781596913560_pages_256.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='One Perfect Day', author=rebecca_mead, genre=GenreChoices.BIO_AUTOBIO, publication_date='2008-05-08', cover_image=image_file_obj, isbn='9781596913560', number_of_pages=256)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/point_of_control_by_drake_green_genre_MYST_THRILL_published_on_7_March_2016_isbn_9781523855809_pages_280.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='Point Of Control', author=drake_green, genre=GenreChoices.MYSTERY_THRILLER, publication_date='2016-03-07', cover_image=image_file_obj, isbn='9781523855809', number_of_pages=280)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/spindle_fire_by_lexa_hillyer_genre_FTSY_published_on_11_April_2017_isbn_9780062440877_pages_368.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='Spindle Fire', author=lexa_hillyer, genre=GenreChoices.FANTASY, publication_date='2017-04-11', cover_image=image_file_obj, isbn='9780062440877', number_of_pages=368)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_art_of_crash_landing_by_melissa_decarlo_genre_FTSY_published_on_8_September_2015_isbn_9780062390547_pages_336.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Art Of Crash Landing', author=melissa_decarlo, genre=GenreChoices.FANTASY, publication_date='2015-09-08', cover_image=image_file_obj, isbn='9780062390547', number_of_pages=336)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_catastrophist_by_lawrence_eduglas_genre_HIST_FIC_published_on_1_January_2007_isbn_9780061451652_pages_320.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Catastrophist', author=lawrence_eduglas, genre=GenreChoices.HISTORICAL_FICTION, publication_date='2007-01-01', cover_image=image_file_obj, isbn='9780061451652', number_of_pages=320)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_death_of_bees_by_lisa_o_donnell_genre_HIST_FIC_published_on_2_January_2013_isbn_9780062209856_pages_336.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Death Of Bees', author=lisa_o_donnell, genre=GenreChoices.HISTORICAL_FICTION, publication_date='2013-01-02', cover_image=image_file_obj, isbn='9780062209856', number_of_pages=336)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_elephant_vanishes_by_haruki_murakami_genre_FTSY_published_on_3_June_1993_isbn_9780679750536_pages_327.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Elephant Vanishes', author=haruki_murakami, genre=GenreChoices.FANTASY, publication_date='1993-06-03', cover_image=image_file_obj, isbn='9780679750536', number_of_pages=327)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_flame_alphabet_by_ben_marcus_genre_DYST_published_on_17_January_2012_isbn_9780307379375_pages_289.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Flame Alphabet', author=ben_marcus, genre=GenreChoices.DYSTOPIAN, publication_date='2012-01-17', cover_image=image_file_obj, isbn='9780307379375', number_of_pages=289)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_gone_world_by_tom_sweterlitsch_genre_SCIFI_published_on_6_February_2018_isbn_9780425278901_pages_400.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Gone World', author=tom_sweterlitsch, genre=GenreChoices.SCI_FI, publication_date='2018-02-06', cover_image=image_file_obj, isbn='9780425278901', number_of_pages=400)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_great_gatsby_by_f_scott_fitzgerald_genre_HIST_FIC_published_on_10_April_1925_isbn_9780743273565_pages_180.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Great Gatsby', author=f_scott_fitzgerald, genre=GenreChoices.HISTORICAL_FICTION, publication_date='1925-04-10', cover_image=image_file_obj, isbn='9780743273565', number_of_pages=180)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_inexplicables_by_cherie_priest_genre_FTSY_published_on_13_November_2012_isbn_9780765329487_pages_368.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Inexplicables', author=cherie_priest, genre=GenreChoices.FANTASY, publication_date='2012-11-13', cover_image=image_file_obj, isbn='9780765329487', number_of_pages=368)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_light_between_oceans_by_m_l_stedman_genre_HIST_FIC_published_on_23_July_2012_isbn_9781451681734_pages_343.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Light Between Oceans', author=m_l_stedman, genre=GenreChoices.HISTORICAL_FICTION, publication_date='2012-07-23', cover_image=image_file_obj, isbn='9781451681734', number_of_pages=343)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_long_drop_by_denise_mina_genre_MYST_THRILL_published_on_2_March_2017_isbn_9781409150628_pages_240.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Long Drop', author=denise_mina, genre=GenreChoices.MYSTERY_THRILLER, publication_date='2017-03-02', cover_image=image_file_obj, isbn='9781409150628', number_of_pages=240)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_nowhere_girls_by_amy_reed_genre_HIST_FIC_published_on_10_October_2017_isbn_9781481481731_pages_408.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Nowhere Girls', author=amy_reed, genre=GenreChoices.HISTORICAL_FICTION, publication_date='2017-10-10', cover_image=image_file_obj, isbn='9781481481731', number_of_pages=408)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_psychopath_test_by_jon_ronson_genre_BIO_AUTOBIO_published_on_12_May_2011_isbn_9781594485754_pages_288.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Psychopath Test', author=jon_ronson, genre=GenreChoices.BIO_AUTOBIO, publication_date='2011-05-12', cover_image=image_file_obj, isbn='9781594485754', number_of_pages=288)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_queen_of_hearts_by_kimmery_martin_genre_ROM_published_on_13_February_2018_isbn_9780399585050_pages_352.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Queen Of Hearts', author=kimmery_martin, genre=GenreChoices.ROMANCE, publication_date='2018-02-13', cover_image=image_file_obj, isbn='9780399585050', number_of_pages=352)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_sisters_brothers_by_patrick_dewitt_genre_HIST_FIC_published_on_15_April_2011_isbn_9780062041265_pages_325.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Sisters Brothers', author=patrick_dewitt, genre=GenreChoices.HISTORICAL_FICTION, publication_date='2011-04-15', cover_image=image_file_obj, isbn='9780062041265', number_of_pages=325)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_snow_child_by_eowyn_ivey_genre_HIST_FIC_published_on_1_February_2012_isbn_9780316175676_pages_389.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Snow Child', author=eowyn_ivey, genre=GenreChoices.HISTORICAL_FICTION, publication_date='2012-02-01', cover_image=image_file_obj, isbn='9780316175676', number_of_pages=389)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_toy_collector_by_james_gunn_genre_HIST_FIC_published_on_13_February_2001_isbn_9781582341344_pages_278.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Toy Collector', author=james_gunn, genre=GenreChoices.HISTORICAL_FICTION, publication_date='2001-02-13', cover_image=image_file_obj, isbn='9781582341344', number_of_pages=278)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_tragedy_paper_by_elizabeth_laban_genre_HIST_FIC_published_on_8_January_2013_isbn_9780375870408_pages_320.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Tragedy Paper', author=elizabeth_laban, genre=GenreChoices.HISTORICAL_FICTION, publication_date='2013-01-08', cover_image=image_file_obj, isbn='9780375870408', number_of_pages=320)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/the_unlikely_pilgrimage_of_harold_fry_by_rachel_joyce_genre_HIST_FIC_published_on_26_July_2012_isbn_9780812993295_pages_336.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='The Unlikely Pilgrimage Of Harold Fry', author=rachel_joyce, genre=GenreChoices.HISTORICAL_FICTION, publication_date='2012-07-26', cover_image=image_file_obj, isbn='9780812993295', number_of_pages=336)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/wink_poppy_midnight_by_april_genevieve_genre_FTSY_published_on_22_March_2016_isbn_9780803740488_pages_256.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='Wink Poppy Midnight', author=april_genevieve, genre=GenreChoices.FANTASY, publication_date='2016-03-22', cover_image=image_file_obj, isbn='9780803740488', number_of_pages=256)

image_path = 'C:/Users/DELL/Documents/WINNIE/DJANGO_SEPT/book_review/book_review_resources/book_cover_pictures/wonderful_world_by_javier_calvo_genre_HIST_FIC_published_on_5_November_2010_isbn_9788481097111_pages_340.jpg'
with open(image_path, 'rb') as image_file:
    image_file_obj = File(image_file)
    Book.objects.create(title='Wonderful World', author=javier_calvo, genre=GenreChoices.HISTORICAL_FICTION, publication_date='2010-11-05', cover_image=image_file_obj, isbn='9788481097111', number_of_pages=340)

