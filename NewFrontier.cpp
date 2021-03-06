#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <utility>
#include <sstream>
#include<map>


std::vector<std::vector<std::string>> best_people = {};
size_t min_people;



int MinimumPeople(std::vector<std::vector<std::string>>undecided_people, std::vector<std::vector<std::string>> included_people, std::vector<std::string> skills, std::map<std::string, int>undecided_left) {
	int mininum_more_people_needed = 0;
	//If current branch already has more than min_people, just return 
	if (included_people.size() >= min_people) {
		return min_people;
	}

	bool already_found_next = false;
	std::string skill_to_find = "";

	//If there are no people left that have a needed skill, just return 
	for (auto skill : undecided_left) {
		if (skill.second == 0) {
			for (auto skill_inner : skills) {
				if (skill.first == skill_inner) {
					return min_people;
				}
			}
		}
		//If there is only one person with a needed skill, we must include them
		else if (skill.second == 1) {
			already_found_next = true;
			skill_to_find = skill.first;
		}
	}

	//If we hit a result, we know that this result must be a new minimum
	if (undecided_people.size() == 0) {
		if (skills.size() == 0) {
			min_people = included_people.size();
			best_people = included_people;
		}
		return min_people;
	}


	int max_needed_skills = 0;
	//This is the iterator pointing to the person which we will add next
	std::vector<std::vector<std::string>>::iterator max_iter = undecided_people.begin();

	//Selects person with most needed skills
	for (std::vector<std::vector<std::string>>::iterator it = undecided_people.begin(); it != undecided_people.end(); it++) {
		//Finds all needed skills for undecided people and returns iterator pointing to max
		int needed_skills = 0;
		bool skill_found = false;
		for (auto skill : skills) {
			for (auto person_skill : *it) {
				if (skill == person_skill) {
					needed_skills += 1;
				}
				if (already_found_next) {
					if (person_skill == skill_to_find) {
						skill_found = true;
					}
				}
			}
		}
		if (skill_found == true) {
			max_iter = it;
			break;
		}
		else if (needed_skills > max_needed_skills && !already_found_next) {
			max_needed_skills = needed_skills;
			max_iter = it;
		}
	}

	if (max_needed_skills != 0) {
		mininum_more_people_needed = int(skills.size()) / int(max_needed_skills);
		if (included_people.size() + mininum_more_people_needed >= min_people) {
			return min_people;
		}
	}

	std::vector<std::string> current_person = *max_iter;
	undecided_people.erase(max_iter);


	for (auto skill : current_person) {
		undecided_left[skill] -= 1;
	}


	///Compute with exclude
	size_t min1 = MinimumPeople(undecided_people, included_people, skills, undecided_left);

	included_people.push_back(current_person);
	for (auto skill : current_person) {
		for (auto skill_inner : skills) {
			if (skill_inner == skill) {
				std::vector <std::string>::iterator i = skills.begin();
				i = find(skills.begin(), skills.end(), skill_inner);
				skills.erase(i);
			}
		}
	}
	///Compute with include
	size_t min2 = MinimumPeople(undecided_people, included_people, skills, undecided_left);

	return std::min(min1, min2);
}



int main() {
	size_t n, k;
	std::cin >> n >> k;
	std::vector<std::string> skills_needed(0);
	std::map<std::string, int>undecided_left;
	for (size_t i = 0; i < k; i++) {
		std::string temp = "";
		std::cin >> temp;
		if (temp != "") {
			skills_needed.push_back(temp);
			undecided_left.insert(std::pair<std::string, int>(temp, 0));
		}
	}

	std::vector<std::vector<std::string>> people(0);
	int num_skills = 0;
	for (size_t j = 0; j < n; j++) {
		std::cin >> num_skills;
		std::vector<std::string>inner(0);
		for (size_t k = 0; k < num_skills; k++) {
			std::string temp = "";
			std::cin >> temp;
			if (temp != "") {
				inner.push_back(temp);
				undecided_left[temp] += 1;
			}
		}
		people.push_back(inner);

	}

	min_people = sizeof(people);
	size_t min_num = MinimumPeople(people, std::vector<std::vector<std::string>>(0), skills_needed, undecided_left);

	std::cout << min_num;

	//	for (std::vector<std::string> person : best_people) {
	//		for (auto skill : person) {
	//
	//			std::cout << skill << std::endl;
	//		}
	//		std::cout << std::endl;
	//	}
}