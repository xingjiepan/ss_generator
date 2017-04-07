#!/usr/bin/env python3

import pytest
import numpy as np

import ss_generator as ssg


def test_build_beta_sheet():
    print("test build beta sheet.")

    theta1 = np.radians(123.9 - 10)
    tau1 = np.radians(165)
    #tau1 = np.radians(180)
    #tau1 = np.radians(195.8)
    theta2 = np.radians(123.9 + 10)

    R, alpha, delta = ssg.beta_sheet.get_ideal_parameters_from_three_internal_coordinates(theta1, tau1, theta2)
    theta1_calc, tau1_calc, theta2_calc, tau2_calc = \
            ssg.beta_sheet.get_internal_coordinates_for_ideal_sheet(R, alpha, delta)

    print("R = {0:.2f}, alpha = {1:.2f}, delta = {2:.2f}".format(R, np.degrees(alpha), np.degrees(delta)))
    print("theta1 = {0:.2f}, theta1_calc = {1:.2f}".format(np.degrees(theta1), np.degrees(theta1_calc)))
    print("tau1 = {0:.2f}, tau1_calc = {1:.2f}".format(np.degrees(tau1), np.degrees(tau1_calc)))
    print("theta2 = {0:.2f}, theta2_calc = {1:.2f}".format(np.degrees(theta2), np.degrees(theta2_calc)))
    print("tau2_calc = {0:.2f}".format(np.degrees(tau2_calc)))

    
    ca_list = ssg.beta_sheet.generate_ideal_beta_sheet_from_internal_coordinates(theta1, tau1, theta2, 20, 5)
    ssg.IO.save_ca_list(ca_list, "ideal_sheet.pdb")