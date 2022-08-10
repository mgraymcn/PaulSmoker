pst = "Paul Smoker&#58; trumpet"
phd = "Phil Haynes&#58; drums"
phdp = phd + " and percussion"
dgb = "Drew Gress&#58; bass"
ssg = "Steve Salerno&#58; guitar"
rrb = "Ron Rohovit&#58; bass"
aba = "Anthony Braxton&#58; alto saxophone"
esb = "Ed Schuller&#58; bass"
hrt = "Herb Robertson&#58; trumpet, valve trombone, E&#9837; tuba"
dtt = "David Taylor&#58; bass trombone"
ddb = "Dominc Duval&#58; bass"

notet = "Paul Smoker Notet"
trio = "Paul Smoker Trio"

paul_smoker_trio = [pst, rrb, phd]
smoker_trio_qb = [pst, aba, rrb, phd]


#engineers
db = "David Baker"
jr = "Jon Rosenberg"
mdg = "Matthew D. Guarnere"



catamount = "Catamount Recording Studios, Cedar Falls, Iowa"

smoker_albums = {
    "Paul Smoker Notet": {
        "name": "notet",
        "see_also": {
            "trio": "Paul Smoker Trio",
            "joint_venture": "Joint Venture",
            "haynes": "with Phil Haynes",
        },
        "albums": {
            "landings": {
                "bandcamp_id": 3667897462,
                "grouping": notet,
                "title": "Landings",
                "year": "2013",
                "label": "Alvas Records",
                "personnel": [pst, ssg, dgb, phd],
                "engineer": jr,
                "date": "July 15 and 16, 2012",
                "location": "Rochester, NY and Lewisburg, PA",
                "purchase_streaming": {
                    "bandcamp_link": "https://paulsmoker.bandcamp.com/album/landings",
                     "spotify": "1LDCFQhgPtaWtogLYCjPTx",
                     "youtube": "OLAK5uy_kBHVGY4w99hyJp92mIPCNK3gjb9YZGyX4",
                     "amazon": "B00H89JUIE"
                }
            },
            "cool_lives": {
                    "bandcamp_id": 3443618873,
                    "grouping": notet,
                    "title": "Cool Lives",
                    "year": "2012",
                    "label": "Alvas Records",
                    "personnel": [pst, ssg, phd],
                    "engineer": jr,
                    "date": "April 27, 2011",
                    "location": "Bucknell Hall, Lewisburg, PA",
                    "purchase_streaming": {"bandcamp_link": "https://paulsmoker.bandcamp.com/album/cool-lives"},
                },
            "notet_bop_shop": {
                "bandcamp_id": 2653296990,
                "grouping": notet,
                "title": "Notet Live at the Bop Shop",
                "year": "2005",
                "label": "Alvas Records",
                "personnel": [pst, ssg, esb, phd],
                "engineer": mdg,
                "date": "December 2, 2003",
                "location": "in concert at The Bop Shop, Rochester, NY",
                "purchase_streaming": {"bandcamp_link": "https://paulsmoker.bandcamp.com/album/notet-live-at-the-bop-shop", }
                },
        }
    },

    "Paul Smoker/Phil Haynes Duo": {
        "name": "smoker_haynes_duo",
        "albums": {
            "it_might_be_spring": {
            "bandcamp_id": 2702984983,
            "grouping": "Paul Smoker/Phil Haynes Duo",
            "title": "It Might Be Spring",
            "year": "2014",
            "label": "Corner Store Productions",
            "personnel": [pst, phd],
            "engineer": "Michael McNeill; mixed/mastered by Jon Rosenberg",
            "date": "June 5, 2011",
            "location": "in concert at Unity Church, Buffalo, NY",
            "purchase_streaming": {
                "bandcamp_link": "https://paulsmoker.bandcamp.com/album/it-might-be-spring",
                "corner_store_jazz": "https://www.cornerstorejazz.com/product/it-might-be-spring/",
            }
            },
        },
    },

        # trio
    "Paul Smoker Trio": {
        "name": "trio",
        "albums": {
            "fables": {
                "cover_image": "genuine_fables.jpg",
                "grouping": trio,
                "title": "Genuine Fables",
                "year": "1993",
                "label": "hatART CD 6126",
                "personnel": paul_smoker_trio,
                "engineer": db,
                "date": "November 20-21, 1988",
                "location": catamount,
                "purchase_streaming": {"tidal": 49850898,
                                       "spotify": "0ecqM1IbkwA2w97spzP0cN",
                                       "amazon": "B013IEKI5G",
                                       "youtube": "OLAK5uy_lmVnLQIq2n2gRfOTMxDyKTYxTavovf4DY",
                                       "apple": "https://music.apple.com/us/artist/paul-smoker-trio/1025009749"}
            },
            "come_rain": {
                "cover_image": "come_rain.jpg",
                "grouping": trio,
                "title": "Come Rain Or Come Shine",
                "year": "1989",
                "personnel": paul_smoker_trio,
                "engineer": db,
                "date": "August 18 and 19, 1986",
                "location": catamount,
                "cover": "Hella Vits"
            },
            "alone": {
                "cover_image": "alone.jpg",
                "grouping": trio,
                "title": "Alone",
                "year": "1988",
                "personnel": paul_smoker_trio,
                "engineer": db,
                "date": "August 18 and 19, 1986",
                "location": catamount,
                "cover": "Paul Smoker"
            },
            "mrr": {
                "cover_image": "mrr.jpg",
                "grouping": trio,
                "title": "Mississippi River Rat",
                "year": "1985",
                "personnel": paul_smoker_trio,
                "engineer": "Martin Wieland",
                "date": "June 16, 1984",
                "location": "Tonstudio Bauer, Ludwigsburg, Germany",
                "cover": "H.L. Lindenmaier"
            },
            "qb": {
                "cover_image": "qb.jpg",
                "grouping": trio,
                "title": "QB",
                "year": "1984",
                "label": "Alvas Records AR-101",
                "personnel": smoker_trio_qb,
                "engineer": "Steve Sargeant",
                "date": "February 10 and 11, 1984",
                "location": "The University of Iowa, Iowa City, IA",
                "cover": "Andrew Smoker"
            }, }
    },

        # miscellaneous
    "other albums as a leader": {
        "name": "other",
        "albums": {
            "duocity": {
                "cover_image": "duocity.jpg",
                "grouping": "Paul Smoker",
                "title": "Duocity in Brass and Wood",
                "year": "2003",
                "label": "Cadence Jazz Records (CJR 1155/56)",
                "personnel": [pst, esb + " (disc 1)", ddb + " (disc 2)"],
                "engineer": mdg,
                "date": "May 18 (disc 1) and October 10 (disc 2), 2001",
                "location": "Bop Shop Records, Rochester, NY"
            },
            "brass_reality": {
                "bandcamp_id": 1760329687,
                "grouping": "Paul Smoker",
                "title": "Brass Reality",
                "year": "2002",
                "label": "Nine Winds 0241",
                "personnel": [pst, hrt, dtt + " and BB&#9837; tuba", phdp],
                "engineer": jr,
                "date": "June, 1997",
                "location": "New York City",
                "purchase_streaming": {
                    "bandcamp_link": "https://paulsmoker.bandcamp.com/album/brass-reality"
                }
            },
            "mirabile_dictu": {
                "cover_image": "mirabile_dictu.jpg",
                "grouping": "Paul Smoker Trio",
                "title": "Mirabile Dictu",
                "year": "2001",
                "label": "CIMP 233",
                "personnel": ['Paul Smoker, trumpet', 'Steve Salerno, guitar', 'Ken Filiano, bass'],
                "engineer": "Marc D. Rusch",
                "date": "September 18 and 19, 2000",
                "location": "The Spirit Room, Rossie, NY",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/mirabile-dictu/27779809", }
            },
            "standard_deviations": {
                "cover_image": "standard_deviations.jpg",
                "grouping": "Paul Smoker Quartet",
                "title": "Standard Deviations",
                "year": "1999",
                "label": "CIMP 186",
                "personnel": ['Paul Smoker: trumpet', 'Steve Salerno: guitar', 'Tomas Ulrich: cello',
                              'Jay Rosen: drums'],
                "engineer": "Marc D. Rusch",
                "date": "September 22 and 23, 1998",
                "location": "The Spirit Room, Rossie, NY",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/standard-deviations/6053399"}
            },
        },
    },
#
    # as a co-leader
    "Paul Smoker/Damon Short Quintet": {
        "name": "smoker_short_quintet",
        "see_also": {
            "go_figure": "Go Figure",
            "all_of_the_above": "All of the Above",
        },
        "albums": {
            "no_stock_options": {
                "bandcamp_id": 4019454349,
                "grouping": "Paul Smoker/Damon Short Quintet",
                "title": "No Stock Options",
                "year": "2007",
                "label": "Nine Winds, NWCD 0241",
                "personnel": ['Damon Short: drums and percussion', 'Paul Smoker: trumpet', 'Ryan Shultz: bass trumpet',
                              'Chuck Burdelik: saxophones &#38; alto clarinet', 'Ken Filiano, bass'],
                "engineer": "David Baker",
                "date": "July 14 &#38; 15, 2004",
                "location": "Rochester, NY",
                "purchase_streaming": {"bandcamp_link": "https://paulsmoker.bandcamp.com/album/no-stock-options",
                 "amazon": "https://www.amazon.com/Stock-Options-Smoker-Damon-Quintet/dp/B0016D017M", }
            },
        }
    },
    "Smoker, Magnuson, Filiano, Grassi": {
        "name": "smoker_magnuson_filiano_grassi",
        "see_also": {
            "grassi": "Lou Grassi's PoBand"
        },
        "albums": {
            "large_music_1": {
            "cover_image": "large_music_1.jpg",
            "grouping": "Smoker/Magnuson/Filiano/Grassi",
            "title": "Large Music, Vol. 1",
            "year": "2001",
            "label": "CIMP 219",
            "personnel": ['Paul Smoker: trumpet', 'Bob Magnuson: tenor and alto saxophones', 'Ken Filiano: bass',
                          'Lou Grassi: drums'],
            "engineer": "Marc D. Rusch",
            "date": "March 6, 2000",
            "location": "The Spirit Room, Rossie, NY",
            "purchase_streaming": {"apple": "https://music.apple.com/us/album/large-music-1/27776768", }
        },
            "large_music_2": {
                "cover_image": "large_music_2.jpg",
                "grouping": "Smoker/Magnuson/Filiano/Grassi",
                "title": "Large Music, Vol. 2",
                "year": "2001",
                "label": "CIMP 226",
                "personnel": ['Paul Smoker: trumpet', 'Bob Magnuson: alto and tenor saxophones', 'Ken Filiano: bass',
                              'Lou Grassi: drums'],
                "engineer": "Marc D. Rusch",
                "date": "March 6 and 7, 2000",
                "location": "The Spirit Room, Rossie, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/large-music-2/27778055"}
            },
        },
    },
    "Paul Smoker/Vinny Golia Quartet": {
        "name": "smoker_golia_quartet",
        "albums": {
            "halloween_sequel": {
            "cover_image": "halloween_sequel.jpg",
            "grouping": "Paul Smoker/Vinny Golia Quartet",
            "title": "Halloween, the Sequel",
            "year": "1998",
            "label": "Nine Winds Records – NWCD0207",
            "personnel": ['Paul Smoker: trumpet', 'Vinny Golia: baritone saxophone, flute', 'Ken Filiano: bass',
                          'Phil Haynes: drums'],
            "engineer": "Carlos Pereira",
            "date": "11/4/97",
            "location": "K Studio, Brooklyn, New York",
        },
            "halloween_96": {
                "cover_image": "halloween_96.jpg",
                "grouping": "Paul Smoker/Vinny Golia Quartet",
                "title": "Halloween '96",
                "year": "1997",
                "label": "CIMP 129",
                "personnel": ['Paul Smoker: trumpet', 'Vinny Golia: baritone saxophone', 'Ken Filiano: bass',
                              'Phil Haynes: drums '],
                "engineer": "Marc D. Rusch",
                "date": "October 30  31, 1996",
                "location": "The Spirit Room, Rossie, NY",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/halloween-96/5604627", }
            },
        }
    },

    "Joint Venture": {
        "name": "joint_venture",
        "albums": {
            "mirrors": {
                "cover_image": "mirrors.jpg",
                "grouping": "Joint Venture",
                "title": "Mirrors",
                "year": "1993",
                "label": "Enja CD 7049 2",
                "personnel": ['Paul Smoker, trumpet', 'Ellery Eskelin, tenor saxophone', 'Drew Gress, bass',
                              'Phil Haynes, drums'],
                "engineer": "David Baker",
                "date": "September 28th and 29th, 1991",
                "location": "Sorcerer Sound, New York City",
                "cover": "Fritz Hagel",
                "purchase_streaming": {"spotify": "5UJWPQWJ1PJf1O8DX67sUW", }
            },
            "ways": {
            "cover_image": "ways.jpg",
            "grouping": "Joint Venture",
            "title": "Ways",
            "year": "1990",
            "label": "Enja CD 6052 2",
            "personnel": ['Paul Smoker, trumpet', 'Ellery Eskelin, tenor saxophone', 'Drew Gress, bass',
                          'Phil Haynes, drums'],
            "engineer": "David Baker",
            "date": "January 17, 1989",
            "location": "Sorcerer Sound, New York City",
            "cover": "Heino Naujoks",
            "purchase_streaming": {"spotify": "5Ml75016hDULsGRVGUqDNd", }
        },
            "joint_venture": {
            "cover_image": "joint_venture.jpg",
            "grouping": "Joint Venture",
            "title": "Joint Venture",
            "year": "1990",
            "label": "Enja 5049",
            "personnel": ['Paul Smoker, trumpet', 'Ellery Eskelin, tenor saxophone', 'Drew Gress, bass',
                          'Phil Haynes, drums'],
            "engineer": "David Baker",
            "date": "March 1987",
            "location": "Sorcerer Sound, New York City",
            "cover": "Lajos Keresztes",
        },
        }
    },

    "with Gregg Bendian": {
        "name": "bendian",
        "albums": {
            "counterparts": {
                "cover_image": "counterparts.jpg",
                "grouping": "Gregg Bendian Project",
                "title": "Counterparts",
                "year": "1996",
                "label": "CIMP 105",
                "personnel": [
                    "Gregg Bendian: drums and percussion",
                    "Mark Dresser: bass",
                    "Paul Smoker: trumpet, flugelhorn",
                    "Vinny Golia: sopranino and bass clarinets"
                ],
                "engineer": "Marc D. Rusch",
                "date": "January 5, 1996",
                "location": "The Spirit Room, Rossie, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/counterparts/5602082", }
    },
        }
    },

    "with Anthony Braxton": {
        "name": "braxton",
        "see_also": {
            "qb": "QB"
        },
        "albums": {  # Anthony Braxton
            "sextet_parker": {
                "bandcamp_id": 3500443540,
                "grouping": "Anthony Braxton Sextet",
                "title": "Sextet (Parker) 1993",
                "year": "2018",
                "label": "New Braxton House NBH907",
                "personnel": ['Anthony Braxton: alto and soprano saxophone, flute, contrabass clarinet, piano',
                              'Ari Brown: tenor and soprano saxophones', 'Paul Smoker: trumpet, flugelhorn',
                              'Misha Mengelberg: piano', 'Joe Fonda: bass',
                              'Pheeroan akLaff: drums (all tracks expect 41-46)', 'Han Bennink: drums (tracks 41-46 only)'],
                "engineer": "Ansgar Ballhorn, Peter Pfister, and Fanny Pfister",
                "date": "October 18-24, 1993",
                "location": "Cologne, Germany; Amsterdam, Holland; Zuerich, Switzerland; Antwerpen, Belgium",
                "cover": "Ye&scedil;im Tosuner",
                "purchase_streaming": {
                    "bandcamp_link": "https://newbraxtonhouse.bandcamp.com/album/sextet-parker-1993", }
            },
            "nine_compositions": {
                "cover_image": "nine_compositions.jpg",
                "grouping": "Anthony Braxton Sextet",
                "title": "Nine Compositions (Hill) 2000",
                "year": "2000",
                "label": "CIMP 236",
                "personnel": ['Anthony Braxton: alto and soprano saxophones',
                              'Steve Lehman: alto saxophone',
                              'Paul Smoker: trumpet',
                              "Kevin O'Neil: guitar",
                              'Andy Eulau: bass',
                              'Kevin Norton: drums'],
                "engineer": "Marc D. Rusch",
                "date": "May 23 and 24, 2000",
                "location": "The Spirit Room, Rossie, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/nine-compositions-hill-2000/27780019", }
            },
            "charlie_parker_project": {
                "cover_image": "charlie_parker_project.jpg",
                "grouping": "Anthony Braxton",
                "title": "Anthony Braxton's Charlie Parker Project",
                "year": "1995 (reissued 2015)",
                "label": "hat ART CD 2-6160",
                "personnel": [
                    'Anthony Braxton: alto and sopranino saxophones, contrabass clarinet',
                    'Ari Brown: tenor and soprano saxophones',
                    'Paul Smoker: trumpet and flugelhorn',
                    'Misha Mengelberg, piano',
                    'Joe Fonda: bass',
                    'Han Bennink: drums (tracks 1-1 to 1-5)',
                    'Pheeroan AkLaff: drums (tracks 2-1 to 2-10)'],
                "engineer": "Ansgar Ballhorn and Peter Pfister",
                "date": "October 21-23, 1993",
                "location": "Zurich, Switzerland and Cologne, Germany",
                "cover": "fuhrer vienna",
                "purchase_streaming": {
                    "tidal": "46688597",
                    "apple": "https://music.apple.com/us/album/anthony-braxtons-charlie-parker-project-1993/990105470",
                    "spotify": "4jGlnFuKEi3O7cxJO2DOB3",
                    "youtube": "OLAK5uy_mMkqC2gktzSTv3tQs7au5YYVC-WKCP63k",
                    "amazon": "B00WSGVVT8",
                }
            },
            "ensemble_victoriaville": {
                "cover_image": "ensemble_victoriaville.jpg",
                "grouping": "Anthony Braxton",
                "title": "Ensemble [Victoriaville] 1993",
                "year": "1988",
                "label": "Les Disques Victo – VICTO 07",
                "personnel": [
                    'Anthony Braxton: woodwinds',
                    'Paul Smoker: trumpet &#38; flugelhorn',
                    'Evan Parker: tenor &#38; soprano saxes',
                    'George Lewis: trombone',
                    'Bobby Naughton: vibraphone',
                    'Joelle Leandre: bass',
                    'Gerry Hemingway: drums and percussion'
                ],
                "engineer": "Richard Lefevre and Serge Richer",
                "date": "October 8, 1988",
                "location": "Victoriaville, Quebec, Canada",
                "cover": "François Bienvenue",
                "purchase_streaming": {
                    "tidal": "97121266",
                     "apple": "https://music.apple.com/us/album/ensemble-victoriaville-1988/423667204",
                     "youtube": "PLd7saDuTHrFlElD76XZ5Lv_ws5P8eXgbQ",
                     "amazon": "B00B7U4ARQ", }
            },
        }
    },

    "with Harris Eisenstadt": {
        "name": "eisenstadt",
        "albums": {
            "jalolu": {
                "cover_image": "jalolu.jpg",
                "grouping": "Harris Eisenstadt Quintet",
                "title": "Jalolu",
                "year": "2004",
                "label": "CIMP 300",
                "personnel": [
                    "Harris Eisenstadt: drums",
                    "Andy Laster: clarinet and baritone saxophones",
                    "Roy Campbell: trumpet, pocket trumpet, flugelhorn",
                    "Paul Smoker: trumpet",
                    "Taylor Ho Bynum: cornet",
                ],
                "engineer": "Marc D. Rusch",
                "date": "October 27 and 28, 2003",
                "location": "The Spirit Room, Rossie, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/jalolu/7244570", }
            },
        }
    },

    "with the Fonda-Stevens Group": {
        "name": "fonda_stevens_group",
        "albums": {
            "live_at_the_bunker": {
                "bandcamp_id": 3128390425,
                "grouping": "The Fonda-Stevens Group",
                "title": "Live At The Bunker",
                "year": "2002",
                "label": "Leo Records LR 301",
                "personnel": [
                    "Joe Fonda: bass",
                    "Michael Jefry Stevens: piano",
                    "Harvey Sorgen: drums",
                    "Paul Smoker: trumpet",
                ],
                "engineer": "Christopher Kern",
                "date": "October 21 and 22, 1999",
                "location": "Bunker Ulmenwall, Bielefeld, Germany",
                "cover": "Eckart Schönlau",
                "purchase_streaming": {"bandcamp_link": "https://michaeljefrystevens.bandcamp.com/album/live-at-the-bunker",
                 "joe_fonda_site": "http://www.joefonda.com/live-at-the-bunker-the-fonda-stevens-group.html",
                 "tidal": "12534543",
                 "apple": "https://music.apple.com/us/album/live-at-the-bunker/27163696",
                 "spotify": "50hKV1JdnNTxDKS2oo6wCE",
                 "youtube": "OLAK5uy_knF5m6YLHR8scIlef9jnDGlIsVJ4bvlGo",
                 "amazon": "B004Y43LZO", }
    }, }
    },

    "with Lou Grassi": {
        "name": "grassi",
        "see_also": {
            "smoker_magnuson_filiano_grassi": "Smoker, Magnuson, Filiano, Grassi"
        },
        "albums": {
            "composed": {
                "cover_image": "composed.jpg",
                "grouping": "Lou Grassi's PoBand with John Tchicai",
                "title": "comPOsed",
                "year": "2002",
                "label": "CIMP 262",
                "personnel":
                    ['Lou Grassi: drums &#38; percussion',
                     'John Tchicai: tenor saxophone, bass clarinet, flute',
                     'Perry Robinson: clarinet',
                     'Paul Smoker: trumpet',
                     'Art Baron: trombone, ocarina, flute, didgeridoo',
                     'Wilber Morris: bass'
                     ],
                "engineer": "Marc D. Rusch",
                "date": "January 14 and 15, 2002",
                "location": "The Spirit Room, Rossie, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/composed/27783304", }
            },
            "joy_of_being": {
                "cover_image": "joy_of_being.jpg",
                "grouping": "Lou Grassi's PoBand with Joseph Jarman",
                "title": "Joy of Being",
                "year": "2001",
                "label": "CIMP 227",
                "personnel": [
                    'Lou Grassi: drums &#38; percussion',
                    'Joseph Jarman: alto saxophone, flute',
                    'Perry Robinson: clarinet',
                    'Paul Smoker: trumpet',
                    'Steve Swell: trombone',
                    'Wilber Morris: bass'
                ],
                "engineer": "Marc D. Rusch",
                "date": "June 12 and 13, 2000",
                "location": "The Spirit Room, Rossie, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/the-joy-of-being/27778313", }
            },
            "po_band_live": {
                "cover_image": "po_band_live.jpg",
                "grouping": "Lou Grassi's PoBand with Marshall Allen",
                "title": "Live at the Knitting Factory Volume 1",
                "year": "2010",
                "label": "Porter Records – PRCD 4051",
                "personnel": [
                    'Lou Grassi: drums &#38; percussion',
                    'Marshall Allen: alto saxophone, flute',
                    'Perry Robinson: clarinet',
                    'Paul Smoker: trumpet',
                    'Steve Swell: trombone',
                    'Wilber Morris: bass'
                ],
                "engineer": "unknown",
                "date": "September 26, 2000",
                "location": "The Knitting Factory, New York, NY",
                "cover": "Karen Tweedy-Holmes",
                "purchase_streaming": {"tidal": "9020117",
                 "spotify": "6wGReB3rdvJlAUp0j5BL5o",
                 "amazon": "B0049YN6V8", }
            },
            "pozest": {
                "cover_image": "pozest.jpg",
                "grouping": "Marshall Allen with Lou Grassi's PoBand",
                "title": "PoZest",
                "year": "2000",
                "label": "CIMP 207",
                "personnel": [
                    'Lou Grassi: drums &#38; percussion',
                    'Marshall Allen: alto saxophone, flute',
                    'Perry Robinson: clarinet',
                    'Paul Smoker: trumpet',
                    'Steve Swell: trombone',
                    'Wilber Morris: bass'
                ],
                "engineer": "Marc D. Rusch",
                "date": "May 10 and 11, 1999",
                "location": "The Spirit Room, Rossie, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/pozest/7165744", }
            },
        }
    },

    "with Burton Greene": {
        "name": "greene",
        "albums": {
            "signs_of_the_times": {
                "cover_image": "signs_of_the_times.jpg",
                "grouping": "Burton Greene Quintet",
                "title": "Signs Of The Times",
                "year": "1006",
                "label": "CIMP 339",
                "personnel": [
                    "Burton Greene: piano",
                    "Russ Nolan: tenor and soprano saxohones, flute",
                    "Paul Smoker: trumpet",
                    "Ed Schuller: bass",
                    "George Schuller: drums",
                ],
                "engineer": "Marc D. Rusch",
                "date": "August 16, 2005",
                "location": "Gilbert Recital Hall, Canton, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/signs-of-the-times/160860148", }
            },
        }
    },

    "with Phil Haynes": {
        "name": "haynes",
        "see_also":{
            "notet": "Paul Smoker Notet",
            "it_might_be_spring": "It Might Be Spring",
            "trio": "Paul Smoker Trio",
            "brass_reality": "Brass Reality",
            "smoker_golia_quartet": "Paul Smoker/Vinny Golia Quartet",
            "joint_venture": "Joint Venture",
        },
        "albums": {
            "live_insurgency": {
            "cover_image": "live_insurgency.jpg",
            "grouping": "Phil Haynes",
            "title": "Live Insurgency (Set 1)",
            "year": "1998",
            "label": "Soul Note – 121302-2",
            "personnel": [
                'Phil Haynes: drums',
                'Paul Smoker: trumpet',
                'Jeff Palmer: organ',
            ],
            "engineer": "Jon Rosenberg",
            "date": "May 8-13, 1996",
            "location": "The Knitting Factory, New York, NY",
            "cover": "Maria Bonandrini",
            "purchase_streaming": {
                "tidal": "203664154",
                "apple": "https://music.apple.com/us/album/live-insurgency-set-1/305842735",
                "spotify": "3P9IBH9NSNWzGZRUWb6A8K",
                "youtube": "OLAK5uy_kYBjyZovCBOoxZ8xZq4d9cKfXOaKxfwZU",
                "amazon": "B09NGPN6HV",
            }
        },
            "4_horn_lore": {
            "cover_image": "4_horn_lore.jpg",
            "grouping": "Phil Haynes's 4 Horns &#38; What?",
            "title": "4 Horn Lore",
            "year": "1992",
            "label": "Open Minds CD 2413-2",
            "personnel": [
                'Phil Haynes: drums and percussion',
                'Paul Smoker: trumpet',
                'Herb Robertson: trumpet, valve trombone, E&#9837; tuba',
                'Andy Laster: alto and baritone saxophones, flute',
                'Ellery Eskelin: tenor saxophone']
            ,
            "engineer": "David Baker",
            "date": "November 24, 1991",
            "location": "Sorceror Sound, New York, NY",
            "cover": "Stephen Clark",
        },
            "4_horns_and_what": {
            "cover_image": "4_horns_and_what.jpg",
            "grouping": "Phil Haynes's 4 Horns &#38; What",
            "title": "4 Horns &#38; What?",
            "year": "1991",
            "label": "Open Minds – OM 2402",
            "personnel": [
                'Phil Haynes: drums, wind chimes',
                'Andy Laster: alto and baritone saxophones, flute, Manhasset light clip',
                'Ellery Eskelin: tenor saxophone, cabasa',
                'Paul Smoker: trumpet, tambourine',
                'Joe Daley: tuba, baritone horn'
            ],
            "engineer": "David Baker",
            "date": "January 1989",
            "location": "Sorceror Sound, New York, NY",
            "cover": "Gravits",
        },
        }
    },

    "with Fred Hess": {
        "name": "hess",
        "albums": {
        "extended_family": {
            "cover_image": "extended_family.jpg",
            "grouping": "Fred Hess Quartet",
            "title": "Extended Family",
            "year": "2003",
            "label": "Tapestry – 76004-2",
            "personnel": [
                "Fred Hess: tenor saxophone",
                "Paul Smoker: trumpet",
                "Ken Filiano: bass",
                "Damon Short: drums",
            ],
            "engineer": "Matt Spaker",
            "date": "July 18-19, 2002",
            "location": "East End Studio, Rochester, NY",
            "cover": "Eric Rucker",
        },
        "exposed": {
            "cover_image": "exposed.jpg",
            "grouping": "Fred Hess Quartet",
            "title": "Exposed",
            "year": "2001",
            "label": "CIMP 249",
            "personnel": [
                "Fred Hess: tenor saxophone",
                "Paul Smoker: trumpet",
                "Ken Filiano: bass",
                "Damon Short: drums",
            ],
            "engineer": "Marc D. Rusch",
            "date": "June 11 and 12, 2001",
            "location": "The Spirit Room, Rossie, NY",
            "cover": "Kara D. Rusch",
            "purchase_streaming": {"apple": "https://music.apple.com/us/album/exposed/27780883", }
        },}
    },

    "with Adam Lane": {
        "name": "lane",
        "albums": {
            "buffalo": {
                "cover_image": "buffalo.jpg",
                "grouping": "Adam Lane Quartet",
                "title": "Buffalo",
                "year": "2007",
                "label": "Cadence Jazz Records 1193",
                "personnel": [
                    "Adam Lane: bass",
                    "Vinny Golia: winds",
                    "Vijay Anderson: drums",
                    "Paul Smoker: trumpet"
                ],
                "engineer": "Steve Baczkowski",
                "date": "February 25, 2005",
                "location": "Soundlab, Buffalo, NY",
                "cover": "Adam Lane",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/buffalo/258630211", }
            },
            "four_beings": {
                "cover_image": "four_beings.jpg",
                "grouping": "Adam Lane Quartet",
                "title": "Fo(u)r Being(s)",
                "year": "2002",
                "label": "CIMP 263",
                "personnel": [
                    "Adam Lane: bass",
                    "John Tchicai: tenor saxophone, voice",
                    "Paul Smoker: trumpet",
                    "Barry Altschul: drums",
                ],
                "engineer": "Marc D. Rusch",
                "date": "January 21 and 22, 2002",
                "location": "The Spirit Room, Rossie, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/fo-u-r-being-s/27783357", }
            },
        }
    },

    "with Scott R. Looney": {
        "name": "looney",
        "albums": {
            "urban_rumination": {
                "bandcamp_id": 2427374946,
                "grouping": "Scott R. Looney",
                "title": "Urban Rumination",
                "year": "2009",
                "label": "META Records 2010",
                "personnel": [
                    "Scott R. Looney: piano",
                    "Oliver Lake: alto saxophone",
                    "Paul Smoker: trumpet",
                    "Lisle Ellis: bass",
                    ],
                "engineer": "Scott Looney",
                "date": "May 28 (live) and 29 (studio), 2005",
                "location": "Oakland, CA",
                "cover": "Mandy Flowers",
                "purchase_streaming": {"bandcamp_link": "https://scottrlooney.bandcamp.com/album/urban-rumination",
                 "tidal": "29672202",
                 "apple": "https://music.apple.com/us/album/urban-ruminations/348767678",
                 "spotify": "7aYHCQUnGTG4H9ZPfIFhwN",
                 "youtube": "OLAK5uy_kMoBJLavTwhsJpcK-ftoUV_KQksuvE85c",
                 "amazon": "B003299ATS", }
        }
        }
     },

    "with Randy McKean": {
        "name": "mckean",
        "albums": {
            "so_dig_this_big_crux": {
                    "cover_image": "so_dig_this_big_crux.jpg",
                    "grouping": "Randy McKean Quartet",
                    "title": "So Dig This Big Crux",
                    "year": "1992",
                    "label": "Rastascan CD BRD-01",
                    "personnel": [
                        "Randy McKean: alto saxophone and bass clarinet",
                        "Paul Smoker: trumpet and flugelhorn",
                        "Drew Gress: bass",
                        "Phil Haynes: drums",
                    ],
                    "engineer": "David Baker",
                    "date": "April 20, 1991",
                    "location": "Westrax Recording Studio, New York, NY",
                    "cover": "",
                    "purchase_streaming": {"tidal": "10295628",
                     "apple": "https://music.apple.com/us/album/so-dig-this-big-crux/259915039",
                     "spotify": "2hbgi1KNsbBtXFJ6fqn5sg",
                     "youtube": "OLAK5uy_lpNTDbQWHrp8yHmuohmYBJ2NzWbD7fBjM", }
                },
        }
    },

    "with Dom Minasi": {
        "name": "minasi",
        "albums": {
            "vampire_revenge": {
                "cover_image": "vampire_revenge.jpg",
                "grouping": "Dom Minasi",
                "title": "The Vamipre's Revenge",
                "year": "2006",
                "label": "CDM Records",
                "personnel": [
                    "Dom Minasi: guitar",
                    "Ken Filiano: bass",
                    "Jackson Krall: drums",
                    "Perry Robinson: clarinet",
                    "Joe Giardullo: soprano saxophone",
                    "Jason Kao Hwang: violin",
                    "Tomas Urlich: cello",
                    "Carol Mennie: voice",
                    "John Gunther: reeds",
                    "Herb Robertson: trumpet",
                    "Steve Swell: trombone",
                    "Francois Grillot: bass",
                    "Ras Moshe: reeds",
                    "Matthew Shipp: piano",
                    "Mark Whitecage: alto saxophone",
                    "Borah Bergman: piano",
                    "Joe McPhee: tenor saxophone",
                    "Paul Smoker: flugelhorn",
                    "Sabir Mateen: tenor saxophone",
                    "Blaise Siwula: alto saxophone",
                    "Peter Ratray: recitative",
                    "Byron Olsen: conductor",
                ],
                "engineer": "Jon Rosenberg",
                "date": "May 12, June 12, September 20, October 7 and 16, 2005",
                "location": "The Studio (5/12, 9/20, 10/7 and 16) and Systems Two (6/12), New York, NY",
                "cover": "Horacio Molina",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/minasi/210717717",
                 "spotify": "1Apov3NOJeXqgngNLqxsi6",
                 "youtube": "OLAK5uy_lyYPfnUaaiuPU1UfpPpwXyXNc746naT40",
                 "amazon": "B0015HIV08", }
            },
        }
    },

    "with Jay Rosen": {
        "name": "rosen",
        "see_also": {
            "standard_deviations": "Standard Deviations"
        },
        "albums": {
            "drums_n_bugles": {
                "cover_image": "drums_n_bugles.jpg",
                "grouping": "Jay Rosen Trio",
                "title": "Drums 'n Bugles",
                "year": "2002",
                "label": "CIMP 253",
                "personnel": [
                    "Jay Rosen: drums",
                    "Paul Smoker: trumpet",
                    "Herb Robertson: trumpet and slide trumpet",
                ],
                "engineer": "Marc D. Rusch",
                "date": "August 7, 2001",
                "location": "The Spirit Room, Rossie, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/drums-n-bugles/27781387", }
            },
            "canticles": {
                "cover_image": "canticles.jpg",
                "grouping": "Jay Rosen Quartet",
                "title": "Canticles for the New Millenium",
                "year": "2000",
                "label": "CIMP 211",
                "personnel": [
                    "Jay Rosen: drums",
                    "Vinny Golia: sopranino, E&#9837;, B&#9837;, and bass clarinets",
                    "Paul Smoker: trumpet",
                    "Mark Whitecage: moosecall, alto and soprano clarinets, alto and soprano saxophones",
                ],
                "engineer": "Marc D. Rusch",
                "date": "September 1 and 2, 1999",
                "location": "The Spirit Room, Rossie, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/canticles-for-the-new-millennium/27774619", }
            },
        }
    },

    "with Dick Schory": {
        "name": "schory",
        "albums": {
            "dick_schory": {
                "cover_image": "dick_schory.jpg",
                "grouping": "Dick Schory",
                "title": "Live at Carnegie Hall",
                "subtitle": "with Gary Burton, Paul Horn, and Joe Morello",
                "year": "1971",
                "label": "Ovation OVQD",
                "personnel": [
                    "Gary Burton: vibraphone",
                    "Paul Horn: flute",
                    "Joe Morello: drums",
                    "Guy Fricano, Paul Smoker, Art Hoyle: trumpets",
                    "Paul Crumbaugh, Steve Galloway, Ralph Craig: trombones",
                    "Roger Rocco: tuba",
                    "Douglas Hill, Ken Strahl: French horns",
                    "Art Lauer, Willard Allem, Bud Doty: woodwinds",
                    "Ronald Elliston: piano",
                    "Jim Atlas: bass",
                    "Ron Steele, Bob White: guitars",
                    "Tom Radtke: drums",
                    "Duane Thamm, John Walker, Mike McClead: percussion",
                ],
                "engineer": "Ron Steele",
                "date": "1970",
                "location": "Carnegie Hall, NY, NY",
                "cover": "none",
                "purchase_streaming": {"tidal": "221317424",
                 "apple": "https://music.apple.com/us/album/resurrection-live-at-carnegie-hall/1614740185",
                 "spotify": "1WPxB7BA7gS4fE65HypkWe",
                 "youtube": "OLAK5uy_leUIyr6gnmbyESfyjoRQcbWBZPJnTFdpo",
                 "amazon": "B09VSGPQ3Y", }
            },
        }
    },

    "with Kristen Shiner McGuire": {
        "name": "kristen_shiner_mcguire",
        "albums": {
            "kristen_sings": {
                "cover_image": "kristen_sings.jpg",
                "grouping": "Kristen Shiner McGuire",
                "title": "Kristen Sings and Plays and Rings",
                "year": "2011",
                "personnel": [
                    "Kristen Shiner McGuire: drums, vibraphone, marimba, voice",
                    "Paul Smoker: trumpet",
                    "Paul Hofmann: piano",
                    "Dave Arenius: bass",
                    "David McGuire: piano",
                ],
                "engineer": "Tim Hull",
                "date": "July 2011",
                "location": "the Studios at Linden Oaks",
                "cover": "none",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/kristen-sings-and-plays-and-rings/479720852",
                 "spotify": "2Roqqa0HKzYz6qpEYv6EbP",
                 "youtube": "OLAK5uy_l1zlybYA2cMIfOaCJo4goSRzD9b79UUhY",
                 "amazon": "B0065IAZ6U", }
            },
        }
    },

    "with Damon Short": {
        "name": "short",
        "see_also": {
            "no_stock_options": "No Stock Options",
            "hess": "albums with Fred Hess"
        },
        "albums": {
            "go_figure": {
                "cover_image": "go_figure.jpg",
                "grouping": "Damon Short",
                "title": "Go Figure",
                "year": "2002",
                "label": "NineWinds CD 0231",
                "personnel": [
                    'Damon Short: drums, percussion',
                    'Paul Smoker: trumpet',
                    'Ryan Shultz: bass trumpet',
                    'Paul Scea: tenor saxophone, flute, bass clarinet',
                    'Chuck Burdelik: saxophones',
                    'Jim Yanda: guitar',
                    'Larry Kohut: bass'
                ],
                "engineer": "David Baker",
                "date": "November 22 and 23, 1997",
                "location": "Studio Media, Evanston, IL",
                "cover": "Jeff Atherton and Vinny Golia",
            },
            "all_of_the_above": {
                "cover_image": "all_of_the_above.jpg",
                "grouping": "Damon Short",
                "title": "all of the above",
                "year": "1990",
                "label": "Southport Records – S-SSD 0028",
                "personnel": [
                    'Damon Short: drums, percussion',
                    'Paul Smoker: trumpet',
                    'Ryan Shultz: bass trumpet',
                    'Paul Scea: tenor saxophone, flute, bass clarinet',
                    'Jeff Newell: alto and soprano saxophones',
                    'Jim Yanda: guitar',
                    'Larry Kohut: bass'
                ],
                "engineer": "David Baker",
                "date": "June 30 and July 1, 1990",
                "location": "Studiomedia, Evanston, IL",
                "cover": "Damon Short",
        },
        }
    },

    "with David Taylor": {
        "name": "taylor",
        "see_also": {
            "brass_reality": "Brass Reality"
        },
        "albums": {
            "atomic_bomb_blues": {
                "cover_image": "atomic_bomb_blues.jpg",
                "grouping": "Dave Taylor Octet",
                "title": "The Atomic Bomb Blues",
                "year": "2014",
                "personnel": [
                    "Dave Taylor: bass trombone and vocals",
                    "Paul Smoker: trumpet, flugelhorn",
                    "Herb robertson: trumpet, valve trombone",
                    "Steve Wilson: clarinet and alto saxophone",
                    "Andy Laster: baritone saxophone and clarinet",
                    "Patience Higgins: baritone saxophone, tenor saxophone, oboe",
                    "Essiet Essiet: bass, Phil Haynes: drums",
                    "Jessica Taylor: vocals",
                ],
                "engineer": "Jon Rosenberg",
                "date": "January 23, 1998",
                "location": "The Knitting Factory, New York, NY",
                "cover": "Ronnie Taylor",
                "purchase_streaming": {"tidal": "48305095",
                 "apple": "https://music.apple.com/us/album/the-atomic-bomb-blues-live/1014743985",
                 "spotify": "7Laf67SdvxJu8L5ORrodEe",
                 "youtube": "OLAK5uy_nY49UdJxw9gxIm_6B5fdPyMRJsosVrCWM",
                 "amazon": "B010R3RQHE", }
            },
            "past_tells": {
                "bandcamp_id": 3363338871,
                "grouping": "David Taylor",
                "title": "Past Tells",
                "year": "1993",
                "label": "New World CD 80436-2",
                "personnel": [
                    "David Taylor: trombone",
                    "Rolf Schulte and Jon Kass: violins",
                    "Louise Shulman: viola",
                    "Gary Schneider: synthesizer",
                    "Fred Sherry: cello",
                    "Lindsey Horner: bass, tape",
                    "Gordon Gottlieb: percussion",
                    "Emily Mitchell: harp",
                    "Jay Branford: alto and baritone saxophones",
                    "Herb Robertson: trumpet, trombone",
                    "Phil Haynes: drums, percussion",
                    "Andy Laster: baritone saxophone",
                    "Marty Ehrlich: tenor and soprano saxophones, clarinet",
                    "Paul Smoker: trumpet, flugelhorn",
                    "Mark Helias: bass",
                    "Ted Rosenthal: harpsichord",
                ],
                "engineer": "Joe Ferla and Jon Rosenberg",
                "date": "",
                "location": "Electric Lady Studios, Power Station, and East Side Sound",
                "cover": "Steve Byram",
                "purchase_streaming": {"bandcamp_link": "https://newworldrecords.bandcamp.com/album/david-taylor-past-tells",
                 "tidal": "11157795",
                 "apple": "https://music.apple.com/us/album/david-taylor-past-tells/395865829",
                 "spotify": "4vy1ScIz2OnmBYwD5DtxaX",
                 "youtube": "OLAK5uy_lNmiRAU1yDKPuLqSWyxioP4IgOsMTZFrQ", }
            }, }
    },

    "CIMPhonia": {
        "name": "cimphonia",
        "albums": {
            "cimphonia1": {
                "cover_image": "cimphonia1.jpg",
                "grouping": "CIMPhonia",
                "title": "CIMPhonia 1998 Part 1",
                "year": "1998",
                "label": "CIMP 173",
                "personnel": [
                    "Paul Smoker: trumpet",
                    "David Prentice: violin",
                    "Joe McPhee: soprano and tenor saxophones, trumpet",
                    "Mark Whitecage: alto and soprano saxophones, alto clarinet",
                    "Dominic Duval: bass",
                    "Peter Kowald: bass",
                    "Jay Rosen: drums &#38; percussion",
                ],
                "engineer": "Marc D. Rusch",
                "date": "May 26 and 27, 1998",
                "location": "The Spirit Room, Rossie, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/cimphonia-1998-pt-1/6051721", }
            },
            "cimphonia2": {
                "cover_image": "cimphonia2.jpg",
                "grouping": "CIMPhonia",
                "title": "CIMPhonia 1998 Part 2",
                "year": "1999",
                "label": "CIMP 178",
                "personnel": [
                    "Paul Smoker: trumpet",
                    "David Prentice: violin",
                    "Joe McPhee: soprano and tenor saxophones, trumpet",
                    "Mark Whitecage: alto and soprano saxophones, alto clarinet",
                    "Dominic Duval: bass",
                    "Peter Kowald: bass",
                    "Jay Rosen: drums &#38; percussion",
                ],
                "engineer": "Marc D. Rusch",
                "date": "May 26 and 27, 1998",
                "location": "The Spirit Room, Rossie, NY",
                "cover": "Kara D. Rusch",
                "purchase_streaming": {"apple": "https://music.apple.com/us/album/cimphonia-1998-pt-2/6052034", }
            },
        }
    }



}

print('<!DOCTYPE html>')
print('<html lang="en">')
print('    <head>')
print('        <meta charset="utf-8">')
print('        <meta name="viewport" content="width=device-width, initial-scale=1">')
print('        <title> Paul Smoker Discography</title>')
print('<link href = "https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" '
      'integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">')
print(        '<link rel="shortcut icon" href="images/IMG_2769.ico">')

print('<link type="text/css" rel="stylesheet" href="css/smoker.css" />')

print('</head>')
print('<body>')
print('\n\n\n')

print('<a name="top"></a>')
print('    <div class="container col-lg-12 col-sm-6">')
print('        <ul class="nav nav-pills">')
print('             <li class="nav-item">')
print('                 <a class="nav-link" href="index.html">home</a>')
print('             </li>')
print('             <li class="nav-item">')
print('                 <a class="nav-link" href="bio.html">bio</a>')
print('             </li>')
print('             <li class="nav-item">')
print('                 <a class="nav-link active" aria-current="page" id="active" href="#">discography</a>')
print('             </li>')
print('             <li class="nav-item">')
print('                 <a class="nav-link" href="press.html">press</a>')
print('             </li>')
print('             <li class="nav-item">')
print('                 <a class="nav-link" href="video.html">video</a>')
print('             </li>')
print('             <li class="nav-item">')
print('                <a class="nav-link" href="contact.html">contact</a>')
print('             </li>')
print('        </ul>')
print('    </div>')

print('\n\n\n')

print("""<a href="#top"><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="#46a8f2" class="bi 
bi-arrow-up-square-fill" viewBox="0 0 16 16"> <path d="M2 16a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 
0 1-2 2H2zm6.5-4.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 
5.707V11.5a.5.5 0 0 0 1 0z"/> </svg></a>""")

print('<div class="container">')
print('<div class="discography_intro offset-sm-1 col-10">')
print('<h1>Paul Smoker Discography</h1>')
print('<div class="row">')
print('<div class="dropdown index col-md-3 col-sm-12">')
print('<button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">')
print('Index')
print('</button>')
print('<ul class="groupings_index dropdown-menu">')
for grouping_name, value in smoker_albums.items():
    print(f'    <a class="dropdown-item" href="#{value["name"]}"><li>{grouping_name}</li></a>')
print('</ul>')
print('</div>')
print('<div class="offset-col-1 col-sm-12 col-md-8">')
print('    <p class="discography_intro_text">')
print("""Paul Smoker's recording career began in the era of the LP, continued through the CD period, and ended during 
the rise of streaming. His performances were documented on various US and international labels as well as artist-released 
editions. Consequently, some recordings are available on some purchase/streaming platforms but not others, 
and some are currently out of print and unavailable to stream. We will strive to update this page as more recordings 
become available.""")
print('    </p>')
print('    <p class="discography_intro_text">')
print("""The discography begins with Paul's albums as a leader, continues with several projects as a co-leader, 
and concludes with his recordings as a sideperson. Use the <strong>"Index"</strong> dropdown menu to navigate quickly 
to recordings and projects of particular interest, and the <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="#46a8f2" class="bi 
bi-arrow-up-square-fill" viewBox="0 0 16 16"> <path d="M2 16a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 
0 1-2 2H2zm6.5-4.5V5.707l2.146 2.147a.5.5 0 0 0 .708-.708l-3-3a.5.5 0 0 0-.708 0l-3 3a.5.5 0 1 0 .708.708L7.5 
5.707V11.5a.5.5 0 0 0 1 0z"/> </svg> icon to return to the top.""")
print('    </p>')
print('</div>')
print('</div>')
print('\n\n\n')
print('</div>')
for grouping_name, value in smoker_albums.items():
    print(f'<div class="grouping row justify-content-center align-items-start" id="{value["name"]}">')
    print(f'    <div class="album_divider col-sm-12 col-lg-3" id="{value["name"]}_divider">')
    print(f'        <div class="row">')
    print(f'            <div class="col-sm-6 col-lg-12">')
    print(f'                <a name="{value["name"]}"><p class="album_divider_text">{grouping_name}</p></a>')
    print(f'            </div>')
    if "see_also" in value:
        print('             <div class="col-sm-6 col-lg-12">')
        print('                 <p>see also:</p>')
        print('                 <ul class="see_also_list">')
        for other_grouping, title in value["see_also"].items():
            print(f'                <a href="#{other_grouping}"><li>{title}</li></a>')
        print('                 </ul>')
        print('             </div>')
    print('         </div>')
    print(f'    </div>')
    print('\n')
    for album_id, metadata in value["albums"].items():
        print(f'    <div class="album offset-sm-1 col-sm-10 col-lg-3 md-auto" id="{album_id}">')
        if "bandcamp_id" in metadata:
            print(f'        <a name="{album_id}"><iframe class="bandcampCover" src="https://bandcamp.com/EmbeddedPlayer/album={metadata["bandcamp_id"]}/size=large/bgcol=ffffff/linkcol=0687f5/tracklist=false/transparent=true/" seamless></iframe></a>')
        if "cover_image" in metadata:
            print(f'            <a name="{album_id}"><img class="albumCover" src="images/{metadata["cover_image"]}" /></a>')
        print(f'            <p class="title">{metadata["title"]}</p>')
        if "subtitle" in metadata:
            print(f'                <p class="subtitle">{metadata["subtitle"]}</p>')
        print(f'            <p class="year">{metadata["year"]}</p>')
        if "label" in metadata:
            print(f'            <p class="label">{metadata["label"]}</p>')
        print("")
        print(f'            <ul class="musiciansList">')
        for musician in metadata["personnel"]:
            print(f'                <li>{musician}</li>')
        print("            </ul>")
        print("")
        print(f'            <p class="engineer">Recorded by {metadata["engineer"]}</p>')
        print(f'            <p class="recordingDate">{metadata["date"]}, ')
        print(f'            {metadata["location"]}</p>')
        if "cover" in metadata:
            print(f'            <p class="coverArt">Cover art by {metadata["cover"]}</p>')
        print('\n')
        if "purchase_streaming" in metadata:
            purchase_streaming = metadata["purchase_streaming"]
            print('            <div class="dropdown purchase_streaming_dropdown">')
            print('            <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">')
            print('            Purchase/Stream')
            print('            </button>')
            print('             <ul class="streamingLinks dropdown-menu">')
            if "bandcamp_link" in purchase_streaming:
                print(f'                <a class="bandcampLink dropdown-item" href="{purchase_streaming["bandcamp_link"]}"><li><em>{metadata["title"]}</em> on Bandcamp</li></a>')
            if "corner_store_jazz" in purchase_streaming:
                print(f'                <a class="corner_store_jazz dropdown-item" href="{purchase_streaming["corner_store_jazz"]}"><li><em>{metadata["title"]}</em> at CornerStore Jazz</li></a>')
            if "joe_fonda_site" in purchase_streaming:
                print(f'                <a class="joe_fonda_site dropdown-item" href="{purchase_streaming["joe_fonda_site"]}"><li><em>{metadata["title"]}</em> Joe Fonda Website</li></a>'"")
            if "tidal" in purchase_streaming:
                print(f'                <a class="tidalLink dropdown-item" href="https://tidal.com/browse/album/{purchase_streaming["tidal"]}"><li><em>{metadata["title"]}</em> on Tidal</li></a>')
            if "spotify" in purchase_streaming:
                print(f'                <a class="spotifyLink dropdown-item" href="https://open.spotify.com/album/{purchase_streaming["spotify"]}"><li><em>{metadata["title"]}</em> on Spotify</li></a>')
            if "apple" in purchase_streaming:
                print(f'                <a class="appleLink dropdown-item" href="{purchase_streaming["apple"]}"><li><em>{metadata["title"]}</em> on Apple Music</li></a>')
            if "amazon" in purchase_streaming:
                print(f'                <a class="amazonLink dropdown-item" href="https://www.amazon.com/music/player/albums/{purchase_streaming["amazon"]}"><li><em>{metadata["title"]}</em> on Amazon</li></a>')
            if "youtube" in purchase_streaming:
                print(f'                <a class="youtubeLink dropdown-item" href="https://youtube.com/playlist?list={purchase_streaming["youtube"]}"><li><em>{metadata["title"]}</em> on Youtube</li></a>')

            print("             </ul>")
            print('             </div>')
        print(f'    </div>')
        print('\n')
    print('</div>')
print('</div>')
print('<script type="text/javascript">')
print("""function load_css(d){var b=window.top.document.getElementsByTagName("link");for(document_css_index=0;document_css_index<b.length;++document_css_index){var a=b[document_css_index];if(a.href==d){return false}}var c=window.top.document.createElement("link");c.rel="stylesheet";c.type="text/css";c.href=d;window.top.document.getElementsByTagName("head")[0].appendChild(c)}function inject_font_styles(g){var f=window.top.document;var c=f.createElement("style");c.setAttribute("type","text/css");if(c.styleSheet){c.styleSheet.cssText=g}else{var e=f.createTextNode(g);c.appendChild(e)}f.getElementsByTagName("head")[0].appendChild(c);}
load_css(/*font_address*/"http://fonts.googleapis.com/css?family=Roboto:300,300italic&subset=latin,latin-ext");inject_font_styles("body,h1,h2,h3,h4,p,ul,li,div,span,a,#body_content p,#body_content div{font-family:"+/*font_family*/"font-family: 'Roboto', sans-serif;"+"}");
""")

print('</script>')
print('<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js">')
print('</script>')

print('<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>')
print('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.min.js" integrity="sha384-ODmDIVzN+pFdexxHEHFBQH3/9/vQ9uori45z4JjnFsRydbmQbmL5t1tQ0culUzyK" crossorigin="anonymous"></script>')
print('</body>')
print('</html>')
