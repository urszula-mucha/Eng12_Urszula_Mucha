#stuff to remember while code is running
max_weight = 20 #single package can fit max 20kg
current_package_weight = 0 #current box weight, so we can decide if more things will fit or not
packages_sent = 0 #Number of boxes we already sent - keep track of how many went out
total_weight_sent = 0 #all kilograms sent together in all boxes
max_unused_capacity = -1 #measuring of boxes where we didn't have any small item, so the box was sent empty. Cant be negative so it works and is an integer type
current_package_number = 1 #count the packages to show which one was the least productive (wasting space)
package_with_max_unused = 0 #which box was packed in the lamest way

#code to actually do stuff
print("How many items do you want to send?")
max_items = int(input()) #tell me how many questions about weight should I generate?

for item in range(max_items):
    print(f"Enter the weight of each item {item + 1} (write 0 to terminate)")
    weight = int(input())
    if weight == 0: #this if gives the option to kill the loop
        break
    if current_package_weight + weight > max_weight: #this level of ifs, checks if new item fits the old box
        packages_sent += 1
        total_weight_sent += current_package_weight
        unused_capacity = max_weight - current_package_weight #20 minus whatever fit the box until possible
        if unused_capacity > max_unused_capacity: #was this more of a waste than previous ones? remember if yes
            max_unused_capacity = unused_capacity #update old wasted value to a new one
            package_with_max_unused = current_package_number #remember the number of the most wasted box

        current_package_number += 1 #opening a new box
        current_package_weight = weight
    else:
        current_package_weight += weight
if current_package_weight > 0: #this level sens the last package if it had any more items
    packages_sent += 1
    total_weight_sent += current_package_weight
    unused_capacity = max_weight - current_package_weight
    if unused_capacity > max_unused_capacity:  # was this more of a waste than previous ones? Checks the new box
        max_unused_capacity = unused_capacity
        package_with_max_unused = current_package_number

total_unused_capacity = packages_sent * max_weight - total_weight_sent #Final math of waste

#what should be shown in the end
print("Summary of boxes sent:")
print(f"Number of packages sent: {packages_sent}")
print(f"Weight of sent packages: {total_weight_sent}kg")
print(f"Unused capacity: {total_unused_capacity}kg")
print(f"Package with most wasted capacity was Package {package_with_max_unused}. It had {max_unused_capacity}kg of wasted space")