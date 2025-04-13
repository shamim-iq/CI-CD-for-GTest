#include "gtest/gtest.h"
extern "C" {
    #include "../include/my_module.h"  // Include your C module header
}

// Test for the add function
TEST(MyModuleTests, AddFunction) {
    EXPECT_EQ(add(2, 3), 5);
    EXPECT_EQ(add(-1, 1), 1); // Incorrect expected value to force failure
    EXPECT_EQ(add(0, 0), 0);
}

// Test for the subtract function
TEST(MyModuleTests, SubtractFunction) {
    EXPECT_EQ(subtract(5, 3), 2);
    EXPECT_EQ(subtract(3, 5), -2);
    EXPECT_EQ(subtract(0, 0), 0);
}

// Test for the multiply function
TEST(MyModuleTests, MultiplyFunction) {
    EXPECT_EQ(multiply(2, 3), 7); // Incorrect expected value to force failure
    EXPECT_EQ(multiply(-2, 3), -6);
    EXPECT_EQ(multiply(0, 5), 0);
}

// Test for edge cases (e.g., large numbers)
TEST(MyModuleTests, EdgeCases) {
    EXPECT_EQ(add(2147483647, 1), 2147483648);  // Assuming 64-bit integers
    EXPECT_EQ(subtract(-2147483648, 1), -2147483649);
}
