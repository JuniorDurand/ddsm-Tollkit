import os

path_to_ddsm = "/content/drive/My Drive/DataSet/figment.csee.usf.edu/pub/DDSM/"

print("teste")
if os.path.isdir(path_to_ddsm):
	print("is dir")  

for root, subFolders, file_names in os.walk(path_to_ddsm):
    for file_name in file_names:
        if ".LJPEG" in file_name:
            ljpeg_path = os.path.join(root, file_name)
            out_path = os.path.join(root, file_name)
            out_path = out_path.split('.LJPEG')[0] + ".jpg"
            
            cmd = './ljpeg.py "{0}" "{1}" --visual --scale 1.0'.format(ljpeg_path, out_path)
            print (cmd)
            os.system(cmd)

print('done')