# MSDS460Assignment2
Part 1: Problem setup
There are quite a few tasks that need to be done for this project. There’s also a couple things to note about the way this project can be looked at. For the purposes of this project, all of the hourly rates for members of the team are the same, at sixty dollars an hour. Differences in pay will be determined by how much each member works. Our team consists of a project manager, front end developer, backend developer, data scientist, and data engineer. The roles of project manager and data scientist will be filled by me. The frontend developer, backend developer, and data engineer will need to be found. Tasks include, Describe product (PM), Develop marketing strategy (PM), Design brochure (PM or FD), Develop product prototype which has the following subtasks: Requirements analysis (PM), Software design(BD and FD), System design(BD and DE), Coding(FD and BD), Write documentation(PM and Devs), Unit testing (FD and BD), System testing (DE and BD), Package deliverables (PM) and then Survey potential market (PM), Develop pricing plan (PM), Develop implementation  plan (PM), Write client proposal (PM). The team member described next to the task is who would be most suited for each task. The frontend developer, backend developer, and data engineer will mostly be working for the developing product prototype task.

Part 2:
For the purposes of the assignment, all of the hourly rates for each member are the same. This means we are looking for the minimum total time. Also as noted in the assignment instructions we are assuming that there are no resource constraints. Meaning there are no constraints on who can work on what task or limits on hours working in a day. In real life there are constraints such as those. We’re going to be disregarding those things but we still have preceding tasks that we need to be careful of. 
Some of the rules that we need to follow. Task A comes before task D and C. Task B could technically be done at the same time as A. Task E needs B and C done first. Task F needs E and D done before. Task G Needs D and B to be completed. Task H needs to be done after F and G are completed. There are subsets within task D that have precedences as well. Task D2 and D3 need to be done after D1. D4 needs D2 and D3 to be done. D5 and D6 need D4 done. D7 needs D6 to be done. D8 needs D5 and D7 to be done. 
The objective function would look something like this which is based on the best case hours.
Minimize Time = max{tA​+8,tB​+16,tC​+16,tD1​+24,tD2​+40,tD3+40,tD4+80,tD5+16,tD6+24,tD7+32,
tD8+16,E+24,F+16,G+24,tH​+16}

Part 4: Solution. 
Best case solution was 240 hours, expected case solution was 392 hours, worst case solution was 568 hours. 
Critical Paths for each scenario
Best: A to D1 to D2 or D3 to D4 to D6 to D7 to D8 to G to H
Expected: A to D1 to D3 to D4 to D6 to D7 to D8 to G to H
Worst: A to D1 to D3 to D4 to D6 to D7 to D8 to G to H

 Part 5: Overview.
The goal of this project is to create a recommendation system for restaurants in Marlborough, Massachusetts, using Yelp reviews for the data. The frontend will be built using Alpine.js and Tailwind, a GraphQL API, and a Go web and database server on the backend. Python will be used for recommender system analytics on the backend, with persistent storage provided by PostgreSQL. Data storage will use PostgreSQL. The entire system will be hosted on AWS.

