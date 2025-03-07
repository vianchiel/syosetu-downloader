import os
import requests
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
queue_path = os.path.join(dir_path, "queue")

class noct_downloader:
    def __init__(self):
        self.id = 0
        self.size = 0
    
    def download(self):
        counter = 0
        for i in range(1, self.size+1):
            url = "None"
            headers = {}
            response = requests.get(
                url,
                headers=headers,
                #cookies=cookies,
                stream=True
            )
            
            #print(response.status_code, response.headers)
            filename = response.headers['Content-Disposition'].split('; ')[1].split('=')[1]
            print(filename)
            with open(os.path.join(queue_path, filename), 'wb') as file:
                for chunk in response.iter_content(chunk_size=16*1024):
                    file.write(chunk)
            
            counter += 1

            if counter >= 10:
                time.sleep(5)
                counter = 0

        reading_queue = []
        all_contents = []

        for (dirpath, dirnames, filenames) in os.walk(queue_path):
            
            sorted_file_names = sorted(filenames, key=lambda x: int(x.split('-')[1].split('.')[0]))
            
            for filename in sorted_file_names:
                reading_queue.append(os.path.join(queue_path,filename))

        for file in reading_queue:
            with open(file, 'r', encoding='utf-8') as file:
                contents = file.read()
                all_contents.append(contents)

        parsed_contents = "\n\n\n\n".join(all_contents)

        with open(str(self.id)+".txt", 'w', encoding='utf-8') as file:
            file.write(parsed_contents)

if __name__ == '__main__':
    main()