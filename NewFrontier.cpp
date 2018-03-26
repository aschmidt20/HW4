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


int MinimumPeople(std::vector<std::vector<std::string>>undecided_people, std::vector<std::vector<std::string>> included_people, std::vector<std::string> skills, std::map<std::string,int>undecided_left) {

	if (included_people.size() >= min_people) {
		return min_people;
	}
	for (auto skill : undecided_left) {
		if (skill.second == 0) {
			for (auto skill_inner : skills) {
				if (skill.first == skill_inner) {
					return min_people;
				}
			}
		}
	}
	if (undecided_people.size() == 0) {
		if (skills.size() == 0) {
				min_people = included_people.size();
				best_people = included_people;
		}
		return min_people;
	}

	std::vector<std::string> current_person = undecided_people.back();
	undecided_people.pop_back();


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
			undecided_left.insert(std::pair<std::string,int>(temp, 0));
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