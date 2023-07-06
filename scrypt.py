from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import random

def generateFinalCSV(childUrls, out):
    n=0
    cnt_arr = [3840,2320,640,240,80,80,960,580,160,60,20,20]
    l=len(childUrls)
    for i in range(0,12):
        for j in range(0,cnt_arr[i]):
            out.write(childUrls[i]+'\n')
            n+=1

    a = ((l-12)/2)-1

    for i in range(0,800):
        ind = random.randint(12,a)
        out.write(childUrls[ind]+'\n')
        n+=1
        
    for i in range(0,200):
        ind = random.randint(a,l-1)
        out.write(childUrls[ind]+'\n')
        n+=1
    
    return n


if __name__ == '__main__' : 

    childUrls=[]
    child = open('child_layers.csv', 'r')

    parser = ArgumentParser("Arguments", formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument("-c","--ads_content_id", help="Content ID for Ads")
    parser.add_argument("-m","--ads_si_match_id", help="Content ID for Ads")

    args = vars(parser.parse_args())

    ads_content_id = args["ads_content_id"]
    ads_si_match_id = args["ads_si_match_id"]

    if ads_content_id is None or ads_content_id == "":
        print("Error : Content ID for Ads is missing.")
        exit(1)
    
    if ads_si_match_id is None or ads_si_match_id == "":
        print("Error : SIMatchID for Ads is missing.")
        exit(1)

    ####################################################################################################################
 
    query_params = '?random=1-inallow-test-2023&content_id={ads_content_id}&language=hindi&resolution=320x180&hash=28ea&bandwidth=169400&media_codec=h264&audio_codec=aac&layer=child&playback_proto=http&playback_host=har-mock-server-dev-internal.npe.hotstar-labs.com&si_match_id={ads_si_match_id}'
    query_params = query_params.format(ads_content_id = ads_content_id, ads_si_match_id = ads_si_match_id)

    for url in child:
        childUrls.append(url.strip()+query_params)
    

    print('\n******************** GOT {n} CHILD LAYERS ***********************************\n'.format(n=len(childUrls)))

    print('> Generating final layes csv ... ')
    final_layer = open('generated/layers_final.csv', 'w')
    n = generateFinalCSV(childUrls,final_layer)
    final_layer.close()

    print('\n******************** GENERATED LAYERS CSV WITH {n} ENTRIES ***************\n'.format(n=n))

    exit(0)

    ####################################################################################################################






