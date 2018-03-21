#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <utility>
#include <sstream>


std::vector<std::string> best_people = {};

bool checkFulfilled(std::vector<std::string>skills, std::vector<std::string>included, size_t num_skills) {
	if (num_skills < skills.size()) {
		return false;
	}
	else {
		return true;
	}
}

int MinimumPeople(std::vector<std::string>skills, std::vector<std::string>undecided_people, std::vector<std::string> included_people, size_t min_people, size_t num_skills) {
	
	if (undecided_people.size() == 0) {
		if (checkFulfilled(skills, included_people, num_skills)) {
			if (included_people.size() < min_people){
				min_people = included_people.size();
				best_people = included_people;
			}
		}
		return min_people;
	}

	std::string current_person = undecided_people.back();
	undecided_people.pop_back();

	///Compute with exclude
	size_t min1 = MinimumPeople(skills, undecided_people, included_people, min_people, num_skills);
	
	included_people.push_back(current_person);
	num_skills += 1;
	///Compute with include
	size_t min2 = MinimumPeople(skills, undecided_people, included_people, min_people, num_skills);

	return std::min(min1, min2);
}



int main() {
	size_t n, k;
	std::cin >> n >> k;

	std::vector<std::string> skills_needed(k);
	for (size_t i = 0; i < k; i++) {
		std::cin >> skills_needed[i];
	}
	std::vector<std::string> people(n);
	int num_skills = 0;
	for (size_t j = 0; j < n; j++) {
		std::cin >> num_skills;
		std::cin >> people[j];
	}
	size_t min_num = MinimumPeople(skills_needed, people, std::vector<std::string>(0), people.size(), 0);

	std::cout << min_num;

	for (std::string person : best_people) {
		std::cout << person << std::endl;
	}
}
	
		
		
		
		
		
		
		