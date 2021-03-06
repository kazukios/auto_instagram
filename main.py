import instagram
import log_util
import csv_util
import settings


def main():
    # デバッグモード
    debug_mode = False

    # setting logger
    logger = log_util.setup_logger(settings.LOG_DIR)

    # web_driverを生成
    driver_util = instagram.driver_util.DriverUtil()

    # Instagramへのアクセス
    instagram_common = instagram.instagram_common.InstagramCommon(driver_util.get_driver(), logger, debug=debug_mode)
    instagram_common.access_instagram()

    mode = 1
    if mode == 1:
        # 自動いいね処理
        auto_like = instagram.instagram_auto_like.InstagramAutoLike(driver_util.get_driver(), logger)
        auto_like.auto_like(csv_util.make_tag_dict())
        # ログアウト
        instagram_common.log_out_instagram()
    else:
        # フォロワー洗い出し処理
        follower = instagram.instagram_follower.InstagramFollower(driver_util.get_driver(), logger)
        follower.access_my_page()
        test = follower.get_follower()


if __name__ == '__main__':
    main()
