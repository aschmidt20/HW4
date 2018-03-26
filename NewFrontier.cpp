#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <utility>
#include <sstream>


std::vector<std::vector<std::string>> best_people = {};
size_t min_people;


int MinimumPeople(std::vector<std::vector<std::string>>undecided_people, std::vector<std::vector<std::string>> included_people, std::vector<std::string> skills) {

	if (included_people.size() > min_people) {
		return min_people;
	}
	if (undecided_people.size() == 0) {
		if (skills.size() == 0) {
			if (included_people.size() < min_people) {
				min_people = included_people.size();
				best_people = included_people;
			}
		}
		return min_people;
	}

	std::vector<std::string> current_person = undecided_people.back();
	undecided_people.pop_back();

	///Compute with exclude
	size_t min1 = MinimumPeople(undecided_people, included_people, skills);

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
	size_t min2 = MinimumPeople(undecided_people, included_people, skills);

	return std::min(min1, min2);
}



int main() {
	size_t n, k;
	std::cin >> n >> k;
	std::vector<std::string> skills_needed(k);
	for (size_t i = 0; i < k; i++) {
		std::string temp = "";
		std::cin >> temp;
		skills_needed.push_back(temp);
	}

	std::vector<std::vector<std::string>> people(n);
	int num_skills = 0;
	for (size_t j = 0; j < n; j++) {
		std::cin >> num_skills;
		std::vector<std::string>inner(num_skills);
		for (size_t k = 0; k < num_skills; k++) {
			std::string temp = "";
			std::cin >> temp;
			inner.push_back(temp);
		}
		people.push_back(inner);

	}

	min_people = sizeof(people);
	size_t min_num = MinimumPeople(people, std::vector<std::vector<std::string>>(0), skills_needed);

	std::cout << min_num;
	//
	//for (std::vector<std::string> person : best_people) {
	//	for (auto skill : person) {
	//		std::cout << skill << std::endl;
	//	}
	//	std::cout << std::endl;
	//}
}