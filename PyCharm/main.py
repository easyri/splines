import time

import PyCharm.quadratic_threading

if __name__ == '__main__':
    # img = plt.imread("mandrill.jpg")
    # step = 2
    # img_array_cutted = np.array(img[::step, ::step].copy(), dtype=np.uint8)
    #
    # # Quadratic
    # start_time = time.time()
    # new_img_quadratic = qs.quadratic_spline(img_array_cutted, img)
    # print("--- %s seconds ---" % (time.time() - start_time))
    #
    # show.show_one(new_img_quadratic, 'quadratic')
    # # show(new_img_quadratic, img, 'quadratic spline image')
    #
    # # Cubic
    # start_time = time.time()
    # new_img_cubic = cs.cubic_spline(img_array_cutted, img)
    # print("--- %s seconds ---" % (time.time() - start_time))
    #
    # show.show_one(new_img_cubic, 'cubic')
    # # show(new_img_cubic, img, 'cubic spline image')

    # # Quadratic + threading TODO
    start_time = time.time()
    PyCharm.quadratic_threading.process_quadratic()
    print("--- %s seconds ---" % (time.time() - start_time))

    # # Cubic + threading TODO
