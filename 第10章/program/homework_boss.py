from uiautomator import Device

device = Device()
resource_id_dict = {
    'salary': 'com.hpbr.bosszhipin:id/tv_position_salary',
    'company': 'com.hpbr.bosszhipin:id/tv_company_name',
    'address': 'com.hpbr.bosszhipin:id/tv_location',
    'experence': 'com.hpbr.bosszhipin:id/tv_work_exp',
    'degree': 'com.hpbr.bosszhipin:id/tv_degree'}


def crawl():
    for job in device(resourceId='com.hpbr.bosszhipin:id/rl_section_1'):
        result_dict = {}
        job_info_box = job.child(resourceId='com.hpbr.bosszhipin:id/ll_position')
        job_name = job_info_box.child(resourceId='com.hpbr.bosszhipin:id/tv_position_name')
        if not job_name.exists:
            return
        result_dict['job_name'] = job_name.text
        for key, resource_id in resource_id_dict.items():
            value = job.child(resourceId=resource_id)
            if not value.exists:
                return
            result_dict[key] = value.text
        print(result_dict)


def scroll():
    device(scrollable=True).scroll.vert.forward()

if __name__ == '__main__':
    while True:
        crawl()
        scroll()
