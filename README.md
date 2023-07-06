
## Cohort Generation

- Run `python3 cohort-generator.py <cohort_size>`

-  `cohort_size` = no of cohorts needed (must be a multiple of 20 for now as initial file contains 20 cohorts)

- new csv `cohorts_final.csv` will be generated

  

## Child Layer URL Generation

* Put child layers generated from mock server in `child_layers.csv`

* Run `python3 scrypt.py --ads_content_id=<ads_content_id> --ads_si_match_id=<ads_si_match_id>`

	 > example : python3 scrypt.py --ads_content_id=1910027536 --ads_si_match_id=112155

*  `ads_content_id` = ContentId on which ads are setup

*  `ads_si_match_id` = MatchID on which ads are setup

* Then it will replicate the child URLs according to the distribution below

- The first 12 layers are replicated as follows

| Layer | Count | Layer | Count |

|--|--|--|--|

| Hindi/Mobile/H265 | 3840 | English/Mobile/H265 | 960 |

| Hindi/Mobile/H264 | 2320 | English/Mobile/H264 | 580 |

| Hindi/TV/H265 | 640 | English/TV/H265 | 160 |

| Hindi/TV/H264 | 240 | English/TV/H264 | 60 |

| Hindi/1080/H265 | 80 | English/1080/H265 | 20 |

| Hindi/1080/H264 | 80 | English/1080/H264 | 20 |

  

- From half (Hindi) of the remaining layers a value is picked 800 times (each time a random value) and from other half (English) a value is picked 200 times (each time a random value).

- Total 10000 layers are generated at `generated/layers_final.csv`.