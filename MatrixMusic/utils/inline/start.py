from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=Commands&admin=ban_users+restrict_members+delete_messages+add_admins+change_info+invite_users+pin_messages+manage_call+manage_chat+manage_video_chats+promote_members",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url="https://t.me/veevvw"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
           InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=Commands&admin=ban_users+restrict_members+delete_messages+add_admins+change_info+invite_users+pin_messages+manage_call+manage_chat+manage_video_chats+promote_members",
            ),
           InlineKeyboardButton(
            text=_["S_B_5"],
            url=f"https://t.me/BDB0B",
        )
        ],
        [
           InlineKeyboardButton(
                text=_["ST_B_3"],
                callback_data="LG"
            ),
           InlineKeyboardButton(
            text=_["S_B_4"],
            callback_data="zzzback"
        )
        ],
        [
             InlineKeyboardButton(
                text=_["S_B_9"],
                url=f"https://t.me/veevvw",
            ),
            InlineKeyboardButton(
                text=_["S_B_6"],
                url="https://t.me/veevvw"
            ),
        ],
    ]
    return buttons
