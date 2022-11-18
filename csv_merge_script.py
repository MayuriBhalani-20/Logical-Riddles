import pandas as pd

import os

original_csv_file_path = os.getcwd() + "/PENDING_Unpopular Ventures Syndicate List.csv"
new_csv_file_path = os.getcwd() + "/Unpopular Ventures Syndicate List1.csv"

old_csv_file = pd.read_csv(original_csv_file_path)
new_csv_file = pd.read_csv(new_csv_file_path)

name_list = list(new_csv_file["Name"].values)
description_list = list(new_csv_file["Title (For now we considered short description)"].values)
linkedin_list = list(new_csv_file["Linked in"].values)
url_list = list(new_csv_file["Profile URL"].values)

old_url_list = list(old_csv_file["Profile URL"].values)
print(len(url_list))
print("len(url_list)////////////////")
count = 1
for i in range(len(old_url_list)):
    for j in range(len(url_list)):
        if old_url_list[i].lower() == url_list[j].lower():
            print("MATCHED================ ", count)
            old_csv_file.loc[i, "Name"] = name_list[j]
            old_csv_file.loc[i, "Title (For now we considered short description)"] = description_list[j]
            old_csv_file.loc[i, "Linked in"] = linkedin_list[j]
            old_csv_file.loc[i, "Profile URL"] = url_list[j]
            count += 1

old_csv_file.to_csv("Unpopular Ventures Syndicate List.csv", index=False)